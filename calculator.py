from config import PAYOUT_MULTIPLIERS

def calculate_potential_payout(bet_type, bet_amount, bet_value=None):
    multiplier = PAYOUT_MULTIPLIERS.get(bet_type, 2)
    return bet_amount * multiplier

def display_calculator():
    from utils import display_separator
    
    while True:
        display_separator()
        print("betting calculator")
        display_separator()
        print("calculate potential payout for different bet types")
        print("\nbet types:")
        print("1. number (0-36) - payout: 36x")
        print("2. color (red/black) - payout: 2x")
        print("3. odd/even - payout: 2x")
        print("4. high/low - payout: 2x")
        print("5. back to main menu")
        
        choice = input("\nselect bet type (1-5): ").strip()
        
        if choice == "5":
            break
        
        if choice not in ["1", "2", "3", "4"]:
            print("invalid choice")
            continue
        
        try:
            amount = int(input("enter bet amount: ").strip())
            if amount <= 0:
                print("bet amount must be positive")
                continue
        except ValueError:
            print("invalid bet amount")
            continue
        
        if choice == "1":
            bet_type = "number"
            try:
                number = int(input("enter number (0-36): ").strip())
                if number < 0 or number > 36:
                    print("number must be between 0 and 36")
                    continue
                bet_value = number
            except ValueError:
                print("invalid number")
                continue
        elif choice == "2":
            bet_type = "color"
            color = input("enter color (red/black): ").strip().lower()
            if color not in ["red", "black"]:
                print("color must be red or black")
                continue
            bet_value = color
        elif choice == "3":
            bet_type = input("enter odd or even: ").strip().lower()
            if bet_type not in ["odd", "even"]:
                print("must be odd or even")
                continue
            bet_value = None
        elif choice == "4":
            bet_type = input("enter high or low: ").strip().lower()
            if bet_type not in ["high", "low"]:
                print("must be high or low")
                continue
            bet_value = None
        
        payout = calculate_potential_payout(bet_type, amount, bet_value)
        profit = payout - amount
        
        display_separator()
        print("calculation results:")
        display_separator()
        print(f"bet amount: ${amount}")
        bet_desc = f"{bet_type}"
        if bet_value is not None:
            bet_desc += f" ({bet_value})"
        print(f"bet type: {bet_desc}")
        print(f"potential payout: ${payout}")
        print(f"potential profit: ${profit}")
        print(f"roi: {(profit/amount)*100:.1f}%")
        display_separator()
        
        input("press enter to continue...")

def compare_bet_types(amount):
    from utils import display_separator
    
    display_separator()
    print("bet type comparison (bet amount: ${})".format(amount))
    display_separator()
    
    bet_types = [
        ("number", "36x", 36),
        ("color", "2x", 2),
        ("odd/even", "2x", 2),
        ("high/low", "2x", 2)
    ]
    
    print(f"{'bet type':<15} {'multiplier':<12} {'payout':<12} {'profit':<12} {'roi':<10}")
    print("-" * 60)
    
    for bet_type, mult_str, multiplier in bet_types:
        payout = amount * multiplier
        profit = payout - amount
        roi = (profit / amount) * 100
        print(f"{bet_type:<15} {mult_str:<12} ${payout:<11} ${profit:<11} {roi:.1f}%")
    
    display_separator()

