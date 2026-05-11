def display_separator():
    """Print a visual separator line."""
    print("-" * 50)

def format_bet_description(bet):
    """Return a compact display string for a bet."""
    bet_desc = f"{bet.bet_type}"
    if bet.bet_type == "dozen" and isinstance(bet.value, tuple):
        bet_desc += f" ({bet.value[0]}-{bet.value[1]})"
    elif bet.value is not None:
        bet_desc += f" ({bet.value})"
    bet_desc += f" - ${bet.amount}"
    return bet_desc

def display_bet_summary(bet):
    """Print a single bet summary with potential payout."""
    from config import PAYOUT_MULTIPLIERS

    display_separator()
    print("bet summary:")
    print(f"type: {format_bet_description(bet)}")
    multiplier = PAYOUT_MULTIPLIERS.get(bet.bet_type, 2)
    potential_payout = bet.amount * multiplier
    print(f"potential payout: ${potential_payout}")
    display_separator()

def format_currency(amount):
    """Format a numeric amount as dollars."""
    return f"${amount}"

def format_percentage(value):
    """Format a numeric value as a percentage."""
    return f"{value:.1f}%"

def format_profit_loss(profit):
    """Format a profit or loss amount with a sign."""
    if profit >= 0:
        return f"+${profit}"
    else:
        return f"-${abs(profit)}"
