ACHIEVEMENTS = {
    'first_win': {'name': 'first win', 'description': 'win your first bet', 'unlocked': False},
    'ten_wins': {'name': 'ten wins', 'description': 'win 10 bets', 'unlocked': False},
    'fifty_bets': {'name': 'fifty bets', 'description': 'place 50 bets', 'unlocked': False},
    'big_winner': {'name': 'big winner', 'description': 'win $5000 in a single session', 'unlocked': False},
    'lucky_streak': {'name': 'lucky streak', 'description': 'win 5 bets in a row', 'unlocked': False},
    'high_roller': {'name': 'high roller', 'description': 'place a bet of $500 or more', 'unlocked': False},
    'perfect_game': {'name': 'perfect game', 'description': 'win rate above 60% with 20+ bets', 'unlocked': False},
    'comeback': {'name': 'comeback', 'description': 'recover from balance below $100', 'unlocked': False}
}

def check_achievements(player, stats, last_bet_won=None):
    unlocked = []
    
    if stats['wins'] >= 1 and not ACHIEVEMENTS['first_win']['unlocked']:
        ACHIEVEMENTS['first_win']['unlocked'] = True
        unlocked.append('first_win')
    
    if stats['wins'] >= 10 and not ACHIEVEMENTS['ten_wins']['unlocked']:
        ACHIEVEMENTS['ten_wins']['unlocked'] = True
        unlocked.append('ten_wins')
    
    if stats['total_bets'] >= 50 and not ACHIEVEMENTS['fifty_bets']['unlocked']:
        ACHIEVEMENTS['fifty_bets']['unlocked'] = True
        unlocked.append('fifty_bets')
    
    if stats['profit'] >= 5000 and not ACHIEVEMENTS['big_winner']['unlocked']:
        ACHIEVEMENTS['big_winner']['unlocked'] = True
        unlocked.append('big_winner')
    
    if player.get_balance() < 100 and stats['profit'] > 0 and not ACHIEVEMENTS['comeback']['unlocked']:
        ACHIEVEMENTS['comeback']['unlocked'] = True
        unlocked.append('comeback')
    
    if stats['total_bets'] >= 20 and stats['win_rate'] >= 60 and not ACHIEVEMENTS['perfect_game']['unlocked']:
        ACHIEVEMENTS['perfect_game']['unlocked'] = True
        unlocked.append('perfect_game')
    
    history = player.get_bet_history()
    if len(history) >= 5:
        last_5 = history[-5:]
        if all(h['won'] for h in last_5) and not ACHIEVEMENTS['lucky_streak']['unlocked']:
            ACHIEVEMENTS['lucky_streak']['unlocked'] = True
            unlocked.append('lucky_streak')
    
    for h in history:
        if h['bet'].amount >= 500 and not ACHIEVEMENTS['high_roller']['unlocked']:
            ACHIEVEMENTS['high_roller']['unlocked'] = True
            unlocked.append('high_roller')
            break
    
    return unlocked

def display_achievements():
    from utils import display_separator
    display_separator()
    print("achievements:")
    display_separator()
    unlocked_count = sum(1 for a in ACHIEVEMENTS.values() if a['unlocked'])
    print(f"unlocked: {unlocked_count}/{len(ACHIEVEMENTS)}\n")
    
    for key, achievement in ACHIEVEMENTS.items():
        status = "✓" if achievement['unlocked'] else "✗"
        print(f"{status} {achievement['name']}: {achievement['description']}")
    display_separator()

def reset_achievements():
    for key in ACHIEVEMENTS:
        ACHIEVEMENTS[key]['unlocked'] = False

