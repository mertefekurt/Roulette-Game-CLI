#!/usr/bin/env python3
import random

RED_NUMBERS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
BLACK_NUMBERS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

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

class Player:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.initial_balance = initial_balance
        self.bet_history = []
        self.wins = 0
        self.losses = 0
    
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
        if won:
            self.wins += 1
        else:
            self.losses += 1
    
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
            'profit': profit
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
    return False

def calculate_payout(bet, winning_number):
    if not check_bet_win(bet, winning_number):
        return 0
    
    if bet.bet_type == "number":
        return bet.amount * 36
    elif bet.bet_type in ["color", "odd", "even", "high", "low"]:
        return bet.amount * 2
    return 0

MINIMUM_BET = 10

def display_separator():
    print("-" * 50)

def format_bet_description(bet):
    bet_desc = f"{bet.bet_type}"
    if bet.value is not None:
        bet_desc += f" ({bet.value})"
    bet_desc += f" - ${bet.amount}"
    return bet_desc

def display_bet_summary(bet):
    display_separator()
    print("bet summary:")
    print(f"type: {format_bet_description(bet)}")
    potential_payout = bet.amount * 36 if bet.bet_type == "number" else bet.amount * 2
    print(f"potential payout: ${potential_payout}")
    display_separator()

def display_menu():
    print("\nbetting options:")
    print("1. number (0-36) - payout: 36x")
    print("2. color (red/black) - payout: 2x")
    print("3. odd/even - payout: 2x")
    print("4. high/low - payout: 2x")
    print("5. view statistics")
    print("6. view bet history")
    print("7. quit")

def get_bet_from_user():
    choice = input("select bet type (1-7): ").strip()
    
    if choice == "7":
        return None
    
    if choice == "5" or choice == "6":
        return choice
    
    if choice not in ["1", "2", "3", "4"]:
        print("invalid choice")
        return None
    
    print("\nquick bet amounts:")
    print("a. $10  b. $50  c. $100  d. $500")
    amount_input = input(f"enter bet amount or quick option (minimum ${MINIMUM_BET}): ").strip().lower()
    
    quick_amounts = {'a': 10, 'b': 50, 'c': 100, 'd': 500}
    if amount_input in quick_amounts:
        amount = quick_amounts[amount_input]
    else:
        try:
            amount = int(amount_input)
            if amount < MINIMUM_BET:
                print(f"bet amount must be at least ${MINIMUM_BET}")
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
    
    return None

def play_game():
    player = Player()
    
    try:
        while True:
            if player.get_balance() <= 0:
                print("\ngame over! you're out of money.")
                return True
            
            print(f"\ncurrent balance: ${player.get_balance()}")
            display_menu()
            
            try:
                bet = get_bet_from_user()
            except KeyboardInterrupt:
                print("\n\ngame interrupted. thanks for playing!")
                return False
            except Exception as e:
                print(f"error: {str(e)}")
                continue
            
            if bet is None:
                print("thanks for playing!")
                return True
            
            if bet == "5":
                stats = player.get_statistics()
                display_separator()
                print("statistics:")
                display_separator()
                print(f"wins: {stats['wins']}")
                print(f"losses: {stats['losses']}")
                print(f"total bets: {stats['total_bets']}")
                print(f"win rate: {stats['win_rate']:.1f}%")
                profit_str = f"+${stats['profit']}" if stats['profit'] >= 0 else f"-${abs(stats['profit'])}"
                print(f"profit: {profit_str}")
                display_separator()
                continue
            
            if bet == "6":
                history = player.get_bet_history()
                display_separator()
                if not history:
                    print("no bet history yet")
                else:
                    print(f"bet history (last {min(5, len(history))} bets):")
                    display_separator()
                    for h in history[-5:]:
                        bet_info = h['bet']
                        bet_desc = f"{bet_info.bet_type}"
                        if bet_info.value is not None:
                            bet_desc += f" ({bet_info.value})"
                        bet_desc += f" - ${bet_info.amount}"
                        result = "won" if h['won'] else "lost"
                        print(f"{bet_desc} -> {result} (landed on {h['winning_number']})")
                display_separator()
                continue
            
            if bet.amount > player.get_balance():
                print("insufficient balance")
                continue
            
            if bet.amount < MINIMUM_BET:
                print(f"bet amount must be at least ${MINIMUM_BET}")
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

