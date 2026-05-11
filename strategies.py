from config import MINIMUM_BET

def _read_base_amount():
    """Read a strategy base amount and clamp it to the table minimum."""
    base = input(f"enter base amount (default ${MINIMUM_BET}): ").strip()
    try:
        base_amount = int(base) if base else MINIMUM_BET
    except ValueError:
        return MINIMUM_BET
    return max(base_amount, MINIMUM_BET)

class BettingStrategy:
    """Base betting strategy that tracks stake size and loss streaks."""

    def __init__(self, name, base_amount=None):
        if base_amount is None:
            base_amount = MINIMUM_BET
        self.name = name
        self.base_amount = base_amount
        self.current_amount = base_amount
        self.consecutive_losses = 0
    
    def get_bet_amount(self):
        """Return the next recommended bet amount."""
        return self.current_amount
    
    def on_win(self):
        self.current_amount = self.base_amount
        self.consecutive_losses = 0
    
    def on_loss(self):
        self.consecutive_losses += 1

class MartingaleStrategy(BettingStrategy):
    """Double the bet amount after each loss."""

    def __init__(self, base_amount=MINIMUM_BET):
        super().__init__("martingale", base_amount)
    
    def on_loss(self):
        super().on_loss()
        self.current_amount = self.base_amount * (2 ** self.consecutive_losses)

class FibonacciStrategy(BettingStrategy):
    """Advance through the Fibonacci sequence after losses."""

    def __init__(self, base_amount=MINIMUM_BET):
        super().__init__("fibonacci", base_amount)
        self.fib_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        self.fib_index = 0
    
    def get_bet_amount(self):
        if self.fib_index >= len(self.fib_sequence):
            return self.fib_sequence[-1] * self.base_amount
        return self.fib_sequence[self.fib_index] * self.base_amount
    
    def on_win(self):
        super().on_win()
        self.fib_index = max(0, self.fib_index - 2)
    
    def on_loss(self):
        super().on_loss()
        self.fib_index = min(len(self.fib_sequence) - 1, self.fib_index + 1)

class ConservativeStrategy(BettingStrategy):
    """Reduce risk after several consecutive losses."""

    def __init__(self, base_amount=MINIMUM_BET):
        super().__init__("conservative", base_amount)
    
    def on_loss(self):
        super().on_loss()
        if self.consecutive_losses >= 3:
            self.current_amount = max(MINIMUM_BET, self.current_amount // 2)
        else:
            self.current_amount = self.base_amount

class DAlembertStrategy(BettingStrategy):
    """Increase after losses and decrease after wins by one base unit."""

    def __init__(self, base_amount=MINIMUM_BET):
        super().__init__("d'alembert", base_amount)
    
    def on_win(self):
        super().on_win()
        self.current_amount = max(MINIMUM_BET, self.current_amount - self.base_amount)
    
    def on_loss(self):
        super().on_loss()
        self.current_amount = self.current_amount + self.base_amount

def get_strategy_from_user():
    """Prompt the player for a betting strategy and base amount."""
    print("\nbetting strategies:")
    print("1. martingale (double bet after loss)")
    print("2. fibonacci (fibonacci sequence)")
    print("3. conservative (reduce after 3 losses)")
    print("4. d'alembert (increase by base on loss, decrease on win)")
    print("5. none (manual betting)")
    
    choice = input("select strategy (1-5): ").strip()
    
    if choice == "1":
        return MartingaleStrategy(_read_base_amount())
    if choice == "2":
        return FibonacciStrategy(_read_base_amount())
    if choice == "3":
        return ConservativeStrategy(_read_base_amount())
    if choice == "4":
        return DAlembertStrategy(_read_base_amount())
    return None
