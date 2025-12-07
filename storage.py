import json
import os

SAVE_FILE = "game_save.json"
LEADERBOARD_FILE = "leaderboard.json"

def save_game_state(player):
    save_data = {
        'balance': player.get_balance(),
        'initial_balance': player.initial_balance,
        'wins': player.wins,
        'losses': player.losses,
        'bet_history': []
    }
    
    for h in player.get_bet_history():
        bet_info = h['bet']
        save_data['bet_history'].append({
            'bet_type': bet_info.bet_type,
            'value': bet_info.value,
            'amount': bet_info.amount,
            'winning_number': h['winning_number'],
            'won': h['won'],
            'payout': h['payout']
        })
    
    try:
        with open(SAVE_FILE, 'w') as f:
            json.dump(save_data, f, indent=2)
        return True
    except Exception as e:
        print(f"error saving game: {str(e)}")
        return False

def load_game_state(player):
    if not os.path.exists(SAVE_FILE):
        return False
    
    try:
        with open(SAVE_FILE, 'r') as f:
            save_data = json.load(f)
        
        player.balance = save_data.get('balance', player.initial_balance)
        player.initial_balance = save_data.get('initial_balance', player.initial_balance)
        player.wins = save_data.get('wins', 0)
        player.losses = save_data.get('losses', 0)
        player.bet_history = []
        
        class Bet:
            def __init__(self, bet_type, value, amount):
                self.bet_type = bet_type
                self.value = value
                self.amount = amount
        
        for h in save_data.get('bet_history', []):
            bet = Bet(h['bet_type'], h['value'], h['amount'])
            player.bet_history.append({
                'bet': bet,
                'winning_number': h['winning_number'],
                'won': h['won'],
                'payout': h['payout']
            })
        
        return True
    except Exception as e:
        print(f"error loading game: {str(e)}")
        return False

def delete_save_file():
    if os.path.exists(SAVE_FILE):
        try:
            os.remove(SAVE_FILE)
            return True
        except Exception as e:
            print(f"error deleting save: {str(e)}")
            return False
    return False

def save_to_leaderboard(player_name, final_balance, profit, total_bets, win_rate):
    leaderboard = load_leaderboard()
    
    entry = {
        'name': player_name,
        'final_balance': final_balance,
        'profit': profit,
        'total_bets': total_bets,
        'win_rate': win_rate
    }
    
    leaderboard.append(entry)
    leaderboard.sort(key=lambda x: x['final_balance'], reverse=True)
    leaderboard = leaderboard[:10]
    
    try:
        with open(LEADERBOARD_FILE, 'w') as f:
            json.dump(leaderboard, f, indent=2)
        return True
    except Exception as e:
        print(f"error saving to leaderboard: {str(e)}")
        return False

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"error loading leaderboard: {str(e)}")
        return []

def display_leaderboard():
    leaderboard = load_leaderboard()
    if not leaderboard:
        print("no leaderboard entries yet")
        return
    
    from utils import display_separator
    display_separator()
    print("top 10 leaderboard:")
    display_separator()
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['name']} - balance: ${entry['final_balance']} | profit: ${entry['profit']} | bets: {entry['total_bets']} | win rate: {entry['win_rate']:.1f}%")
    display_separator()

