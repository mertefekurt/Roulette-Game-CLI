#!/usr/bin/env python3
import random
from config import (
    RED_NUMBERS, BLACK_NUMBERS, MINIMUM_BET, MAXIMUM_BET, INITIAL_BALANCE,
    LOW_BALANCE_WARNING, CRITICAL_BALANCE_WARNING, QUICK_BET_AMOUNTS,
    PAYOUT_MULTIPLIERS
)
from utils import (
    display_separator, format_bet_description, display_bet_summary,
    format_currency, format_percentage, format_profit_loss
)
from storage import save_game_state, load_game_state, save_exists, save_to_leaderboard, display_leaderboard, export_statistics

def spin_wheel():
    return random.randint(0, 36)

def get_number_color(number):
    if number == 0:
        return "green"
    elif number in RED_NUMBERS:
        return "red"
    else:
        return "black"

def check_color_bet(winning_number, bet_color):
    if winning_number == 0:
        return False
    return get_number_color(winning_number) == bet_color.lower()

def check_odd_even_bet(winning_number, bet_type):
    if winning_number == 0:
        return False
    if bet_type == "odd":
        return winning_number % 2 == 1
    else:
        return winning_number % 2 == 0

def check_high_low_bet(winning_number, bet_type):
    if winning_number == 0:
        return False
    if bet_type == "low":
        return 1 <= winning_number <= 18
    else:
        return 19 <= winning_number <= 36

def check_dozen_bet(winning_number, dozen_range):
    if winning_number == 0:
        return False
    start, end = dozen_range
    return start <= winning_number <= end

class Player:
    def __init__(self, initial_balance=None):
        if initial_balance is None:
            initial_balance = INITIAL_BALANCE
        self.balance = initial_balance
        self.initial_balance = initial_balance
        self.bet_history = []
        self.wins = 0
        self.losses = 0
        self.current_win_streak = 0
        self.current_loss_streak = 0
        self.max_win_streak = 0
        self.max_loss_streak = 0
        self.number_frequency = {}
    
    def get_balance(self):
        return self.balance
    
    def add_balance(self, amount):
        self.balance += amount
    
    def subtract_balance(self, amount):
        self.balance -= amount
    
    def add_bet_to_history(self, bet, winning_number, won, payout):
        self.bet_history.append({
            'bet': bet,
            'winning_number': winning_number,
            'won': won,
            'payout': payout
        })
        
        self.number_frequency[winning_number] = self.number_frequency.get(winning_number, 0) + 1
        
        if won:
            self.wins += 1
            self.current_win_streak += 1
            self.current_loss_streak = 0
            if self.current_win_streak > self.max_win_streak:
                self.max_win_streak = self.current_win_streak
        else:
            self.losses += 1
            self.current_loss_streak += 1
            self.current_win_streak = 0
            if self.current_loss_streak > self.max_loss_streak:
                self.max_loss_streak = self.current_loss_streak
    
    def get_hot_numbers(self, count=5):
        if not self.number_frequency:
            return []
        sorted_numbers = sorted(self.number_frequency.items(), key=lambda x: x[1], reverse=True)
        return sorted_numbers[:count]
    
    def get_bet_history(self):
        return self.bet_history
    
    def get_statistics(self):
        total_bets = self.wins + self.losses
        win_rate = (self.wins / total_bets * 100) if total_bets > 0 else 0
        profit = self.balance - self.initial_balance
        return {
            'wins': self.wins,
            'losses': self.losses,
            'total_bets': total_bets,
            'win_rate': win_rate,
            'profit': profit,
            'current_win_streak': self.current_win_streak,
            'current_loss_streak': self.current_loss_streak,
            'max_win_streak': self.max_win_streak,
            'max_loss_streak': self.max_loss_streak
        }

class Bet:
    def __init__(self, bet_type, value, amount):
        self.bet_type = bet_type
        self.value = value
        self.amount = amount

def check_bet_win(bet, winning_number):
    if bet.bet_type == "number":
        return winning_number == bet.value
    elif bet.bet_type == "color":
        return check_color_bet(winning_number, bet.value)
    elif bet.bet_type == "odd" or bet.bet_type == "even":
        return check_odd_even_bet(winning_number, bet.bet_type)
    elif bet.bet_type == "high" or bet.bet_type == "low":
        return check_high_low_bet(winning_number, bet.bet_type)
    elif bet.bet_type == "dozen":
        return check_dozen_bet(winning_number, bet.value)
    return False

def calculate_payout(bet, winning_number):
    if not check_bet_win(bet, winning_number):
        return 0
    
    multiplier = PAYOUT_MULTIPLIERS.get(bet.bet_type, 2)
    return bet.amount * multiplier

def display_menu():
    print("\nbetting options:")
    print("1. number (0-36) - payout: 36x")
    print("2. color (red/black) - payout: 2x")
    print("3. odd/even - payout: 2x")
    print("4. high/low - payout: 2x")
    print("5. dozen (1-12 / 13-24 / 25-36) - payout: 3x")
    print("6. multiple bets (bet on multiple options)")
    print("r. repeat last bet")
    print("7. view statistics")
    print("8. view bet history")
    print("9. view hot numbers")
    print("s. save game")
    print("l. load game")
    print("b. view leaderboard")
    print("c. export statistics to file")
    print("0. quit")

def get_multiple_bets():
    bets = []
    total_amount = 0
    
    print("\ncreate multiple bets (enter 'done' when finished):")
    while True:
        print(f"\ncurrent bets: {len(bets)} | total amount: ${total_amount}")
        print("1. number  2. color  3. odd/even  4. high/low")
        bet_choice = input("select bet type (or 'done'): ").strip().lower()
        
        if bet_choice == "done":
            if len(bets) == 0:
                print("no bets added")
                return None
            break
        
        if bet_choice not in ["1", "2", "3", "4"]:
            print("invalid choice")
            continue
        
        amount_input = input(f"enter bet amount (minimum ${MINIMUM_BET}, maximum ${MAXIMUM_BET}): ").strip().lower()
        if amount_input in QUICK_BET_AMOUNTS:
            amount = QUICK_BET_AMOUNTS[amount_input]
        else:
            try:
                amount = int(amount_input)
                if amount < MINIMUM_BET:
                    print(f"bet amount must be at least ${MINIMUM_BET}")
                    continue
                if amount > MAXIMUM_BET:
                    print(f"bet amount cannot exceed ${MAXIMUM_BET}")
                    continue
            except ValueError:
                print("invalid bet amount")
                continue
        
        if bet_choice == "1":
            number = input("enter number (0-36): ").strip()
            try:
                number = int(number)
                if number < 0 or number > 36:
                    print("number must be between 0 and 36")
                    continue
                bets.append(Bet("number", number, amount))
                total_amount += amount
            except ValueError:
                print("invalid number")
                continue
        elif bet_choice == "2":
            color = input("enter color (red/black): ").strip().lower()
            if color not in ["red", "black"]:
                print("color must be red or black")
                continue
            bets.append(Bet("color", color, amount))
            total_amount += amount
        elif bet_choice == "3":
            oe = input("enter odd or even: ").strip().lower()
            if oe not in ["odd", "even"]:
                print("must be odd or even")
                continue
            bets.append(Bet(oe, None, amount))
            total_amount += amount
        elif bet_choice == "4":
            hl = input("enter high or low: ").strip().lower()
            if hl not in ["high", "low"]:
                print("must be high or low")
                continue
            bets.append(Bet(hl, None, amount))
            total_amount += amount
    
    return bets

def get_bet_from_user(last_bet=None):
    choice = input("select bet type (0-9, a-c, r): ").strip().lower()
    
    if choice == "0":
        return None
    
    if choice == "r":
        if last_bet is None:
            print("no previous bet to repeat")
            return "repeat_unavailable"
        print(f"repeating last bet: {format_bet_description(last_bet)}")
        return Bet(last_bet.bet_type, last_bet.value, last_bet.amount)
    
    if choice in ["6", "7", "8", "9", "s", "l", "b", "c"]:
        return choice
    
    if choice not in ["1", "2", "3", "4", "5"]:
        print("invalid choice")
        return None
    
    print("\nquick bet amounts:")
    print("a. $10  b. $50  c. $100  d. $500")
    amount_input = input(f"enter bet amount or quick option (minimum ${MINIMUM_BET}, maximum ${MAXIMUM_BET}): ").strip().lower()
    
    if amount_input in QUICK_BET_AMOUNTS:
        amount = QUICK_BET_AMOUNTS[amount_input]
    else:
        try:
            amount = int(amount_input)
            if amount < MINIMUM_BET:
                print(f"bet amount must be at least ${MINIMUM_BET}")
                return None
            if amount > MAXIMUM_BET:
                print(f"bet amount cannot exceed ${MAXIMUM_BET}")
                return None
            if amount <= 0:
                print("bet amount must be positive")
                return None
        except ValueError:
            print("invalid bet amount")
            return None
    
    if choice == "1":
        number = input("enter number (0-36): ").strip()
        try:
            number = int(number)
            if number < 0 or number > 36:
                print("number must be between 0 and 36")
                return None
            return Bet("number", number, amount)
        except ValueError:
            print("invalid number")
            return None
    elif choice == "2":
        color = input("enter color (red/black): ").strip().lower()
        if color not in ["red", "black"]:
            print("color must be red or black")
            return None
        return Bet("color", color, amount)
    elif choice == "3":
        oe = input("enter odd or even: ").strip().lower()
        if oe not in ["odd", "even"]:
            print("must be odd or even")
            return None
        return Bet(oe, None, amount)
    elif choice == "4":
        hl = input("enter high or low: ").strip().lower()
        if hl not in ["high", "low"]:
            print("must be high or low")
            return None
        return Bet(hl, None, amount)
    elif choice == "5":
        dozen_input = input("choose dozen (1-12 / 13-24 / 25-36) [1/2/3]: ").strip().lower()
        dozen_options = {
            "1": (1, 12),
            "1st": (1, 12),
            "first": (1, 12),
            "2": (13, 24),
            "2nd": (13, 24),
            "second": (13, 24),
            "3": (25, 36),
            "3rd": (25, 36),
            "third": (25, 36)
        }
        if dozen_input not in dozen_options:
            print("invalid dozen selection")
            return None
        return Bet("dozen", dozen_options[dozen_input], amount)
    
    return None

def check_balance_warnings(balance):
    if balance < CRITICAL_BALANCE_WARNING:
        print("warning: low balance!")
    elif balance < LOW_BALANCE_WARNING:
        print("caution: balance is getting low")

def play_game():
    player = Player()
    
    try:
        if save_exists():
            choice = input("saved game detected. load it? (yes/no): ").strip().lower()
            if choice in ["yes", "y"]:
                if load_game_state(player):
                    print("save loaded. welcome back!")
                else:
                    print("failed to load saved game")
    except KeyboardInterrupt:
        print("\n\ngame interrupted during startup. thanks for playing!")
        return False
    
    try:
        while True:
            if player.get_balance() <= 0:
                save_game_state(player)
                print("\ngame over! you're out of money.")
                return True
            
            balance = player.get_balance()
            print(f"\ncurrent balance: ${balance}")
            check_balance_warnings(balance)
            display_menu()
            
            last_bet = player.bet_history[-1]['bet'] if player.bet_history else None
            
            try:
                bet = get_bet_from_user(last_bet)
            except KeyboardInterrupt:
                print("\n\ngame interrupted. thanks for playing!")
                return False
            except Exception as e:
                print(f"error: {str(e)}")
                continue
            
            if bet is None:
                stats = player.get_statistics()
                display_separator()
                print("session summary:")
                display_separator()
                print(f"starting balance: {format_currency(player.initial_balance)}")
                print(f"ending balance: {format_currency(player.get_balance())}")
                print(f"total bets: {stats['total_bets']}")
                print(f"wins: {stats['wins']} | losses: {stats['losses']}")
                print(f"win rate: {format_percentage(stats['win_rate'])}")
                print(f"profit/loss: {format_profit_loss(stats['profit'])}")
                print(f"max win streak: {stats['max_win_streak']} | max loss streak: {stats['max_loss_streak']}")
                display_separator()
                
                if stats['total_bets'] > 0:
                    player_name = input("enter your name for leaderboard (or press enter to skip): ").strip()
                    if player_name:
                        save_to_leaderboard(
                            player_name,
                            player.get_balance(),
                            stats['profit'],
                            stats['total_bets'],
                            stats['win_rate']
                        )
                        print("saved to leaderboard!")
                
                save_game_state(player)
                print("thanks for playing!")
                return True
            
            if bet == "repeat_unavailable":
                continue
            
            if bet == "5":
                # single dozen bet handled below as normal bet
                pass
            
            if bet == "6":
                multiple_bets = get_multiple_bets()
                if multiple_bets is None:
                    continue
                
                total_bet_amount = sum(b.amount for b in multiple_bets)
                if total_bet_amount > player.get_balance():
                    print("insufficient balance for all bets")
                    continue
                
                for b in multiple_bets:
                    if b.amount > MAXIMUM_BET:
                        print(f"one or more bets exceed maximum bet limit of ${MAXIMUM_BET}")
                        continue
                
                display_separator()
                print("multiple bets summary:")
                for i, b in enumerate(multiple_bets, 1):
                    print(f"{i}. {format_bet_description(b)}")
                print(f"total bet amount: ${total_bet_amount}")
                display_separator()
                
                confirm = input("confirm all bets? (yes/no): ").strip().lower()
                if confirm not in ["yes", "y"]:
                    print("bets cancelled")
                    continue
                
                player.subtract_balance(total_bet_amount)
                winning_number = spin_wheel()
                color = get_number_color(winning_number)
                
                display_separator()
                print(f"spinning... the ball lands on {winning_number} ({color})")
                display_separator()
                
                total_payout = 0
                for b in multiple_bets:
                    payout = calculate_payout(b, winning_number)
                    if payout > 0:
                        total_payout += payout
                        print(f"won on {format_bet_description(b)}: ${payout}")
                
                if total_payout > 0:
                    print(f"total winnings: ${total_payout}!")
                    player.add_balance(total_payout)
                else:
                    print("all bets lost!")
                display_separator()
                
                for b in multiple_bets:
                    payout = calculate_payout(b, winning_number)
                    won = payout > 0
                    player.add_bet_to_history(b, winning_number, won, payout)
                continue
            
            if bet == "7":
                stats = player.get_statistics()
                display_separator()
                print("statistics:")
                display_separator()
                print(f"wins: {stats['wins']}")
                print(f"losses: {stats['losses']}")
                print(f"total bets: {stats['total_bets']}")
                print(f"win rate: {format_percentage(stats['win_rate'])}")
                print(f"profit: {format_profit_loss(stats['profit'])}")
                print(f"current win streak: {stats['current_win_streak']}")
                print(f"current loss streak: {stats['current_loss_streak']}")
                print(f"max win streak: {stats['max_win_streak']}")
                print(f"max loss streak: {stats['max_loss_streak']}")
                display_separator()
                continue
            
            if bet == "8":
                history = player.get_bet_history()
                display_separator()
                if not history:
                    print("no bet history yet")
                else:
                    print(f"bet history (last {min(5, len(history))} bets):")
                    display_separator()
                    for h in history[-5:]:
                        bet_info = h['bet']
                        bet_desc = format_bet_description(bet_info)
                        result = "won" if h['won'] else "lost"
                        print(f"{bet_desc} -> {result} (landed on {h['winning_number']})")
                display_separator()
                continue
            
            if bet == "9":
                hot_numbers = player.get_hot_numbers(5)
                display_separator()
                if not hot_numbers:
                    print("no numbers spun yet")
                else:
                    print("hot numbers (most frequent):")
                    display_separator()
                    for i, (number, count) in enumerate(hot_numbers, 1):
                        color = get_number_color(number)
                        print(f"{i}. {number} ({color}) - appeared {count} time{'s' if count > 1 else ''}")
                display_separator()
                continue
            
            if bet == "s":
                if save_game_state(player):
                    print("game saved successfully!")
                else:
                    print("failed to save game")
                continue
            
            if bet == "l":
                if load_game_state(player):
                    print("game loaded successfully!")
                else:
                    print("no saved game found")
                continue
            
            if bet == "b":
                display_leaderboard()
                continue
            
            if bet == "c":
                filename = input("enter filename (default: statistics.txt): ").strip()
                if not filename:
                    filename = "statistics.txt"
                if export_statistics(player, filename):
                    print(f"statistics exported to {filename}!")
                else:
                    print("failed to export statistics")
                continue
            
            if bet.amount > player.get_balance():
                print("insufficient balance")
                continue
            
            if bet.amount < MINIMUM_BET:
                print(f"bet amount must be at least ${MINIMUM_BET}")
                continue
            
            if bet.amount > MAXIMUM_BET:
                print(f"bet amount cannot exceed ${MAXIMUM_BET}")
                continue
            
            display_bet_summary(bet)
            confirm = input("confirm bet? (yes/no): ").strip().lower()
            if confirm not in ["yes", "y"]:
                print("bet cancelled")
                continue
            
            player.subtract_balance(bet.amount)
            winning_number = spin_wheel()
            color = get_number_color(winning_number)
            
            display_separator()
            print(f"spinning... the ball lands on {winning_number} ({color})")
            display_separator()
            
            payout = calculate_payout(bet, winning_number)
            won = payout > 0
            if won:
                print(f"you win ${payout}!")
                player.add_balance(payout)
            else:
                print("you lose!")
            display_separator()
            
            player.add_bet_to_history(bet, winning_number, won, payout)
    except KeyboardInterrupt:
        print("\n\ngame interrupted. thanks for playing!")
        save_game_state(player)
        return False
    except Exception as e:
        print(f"\nunexpected error: {str(e)}")
        return False

def main():
    print("welcome to roulette!")
    
    while True:
        play_again = play_game()
        
        if not play_again:
            break
        
        try:
            restart = input("\nplay again? (yes/no): ").strip().lower()
            if restart not in ["yes", "y"]:
                print("thanks for playing!")
                break
        except KeyboardInterrupt:
            print("\n\nthanks for playing!")
            break

if __name__ == "__main__":
    main()

