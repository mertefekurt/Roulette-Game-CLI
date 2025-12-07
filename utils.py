def display_separator():
    print("-" * 50)

def format_bet_description(bet):
    bet_desc = f"{bet.bet_type}"
    if bet.value is not None:
        bet_desc += f" ({bet.value})"
    bet_desc += f" - ${bet.amount}"
    return bet_desc

def display_bet_summary(bet):
    from config import PAYOUT_MULTIPLIERS
    display_separator()
    print("bet summary:")
    print(f"type: {format_bet_description(bet)}")
    multiplier = PAYOUT_MULTIPLIERS.get(bet.bet_type, 2)
    potential_payout = bet.amount * multiplier
    print(f"potential payout: ${potential_payout}")
    display_separator()

def format_currency(amount):
    return f"${amount}"

def format_percentage(value):
    return f"{value:.1f}%"

def format_profit_loss(profit):
    if profit >= 0:
        return f"+${profit}"
    else:
        return f"-${abs(profit)}"

