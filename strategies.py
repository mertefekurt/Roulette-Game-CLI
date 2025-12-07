from config import MINIMUM_BET

class BettingStrategy:
    def __init__(self, name, base_amount=None):
        if base_amount is None:
            base_amount = MINIMUM_BET
        self.name = name
        self.base_amount = base_amount
        self.current_amount = base_amount
        self.consecutive_losses = 0
    
    def get_bet_amount(self):
        return self.current_amount
    
    def on_win(self):
        self.current_amount = self.base_amount
        self.consecutive_losses = 0
    
    def on_loss(self):
        self.consecutive_losses += 1

class MartingaleStrategy(BettingStrategy):
    def __init__(self, base_amount=MINIMUM_BET):
        super().__init__("martingale", base_amount)
    
    def on_loss(self):
        super().on_loss()
        self.current_amount = self.base_amount * (2 ** self.consecutive_losses)

class FibonacciStrategy(BettingStrategy):
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
    def __init__(self, base_amount=MINIMUM_BET):
        super().__init__("conservative", base_amount)
    
    def on_loss(self):
        super().on_loss()
        if self.consecutive_losses >= 3:
            self.current_amount = max(MINIMUM_BET, self.current_amount // 2)
        else:
            self.current_amount = self.base_amount

def get_strategy_from_user():
    print("\nbetting strategies:")
    print("1. martingale (double bet after loss)")
    print("2. fibonacci (fibonacci sequence)")
    print("3. conservative (reduce after 3 losses)")
    print("4. none (manual betting)")
    
    choice = input("select strategy (1-4): ").strip()
    
    if choice == "1":
        base = input(f"enter base amount (default ${MINIMUM_BET}): ").strip()
        try:
            base_amount = int(base) if base else MINIMUM_BET
            if base_amount < MINIMUM_BET:
                base_amount = MINIMUM_BET
        except ValueError:
            base_amount = MINIMUM_BET
        return MartingaleStrategy(base_amount)
    elif choice == "2":
        base = input(f"enter base amount (default ${MINIMUM_BET}): ").strip()
        try:
            base_amount = int(base) if base else MINIMUM_BET
            if base_amount < MINIMUM_BET:
                base_amount = MINIMUM_BET
        except ValueError:
            base_amount = MINIMUM_BET
        return FibonacciStrategy(base_amount)
    elif choice == "3":
        base = input(f"enter base amount (default ${MINIMUM_BET}): ").strip()
        try:
            base_amount = int(base) if base else MINIMUM_BET
            if base_amount < MINIMUM_BET:
                base_amount = MINIMUM_BET
        except ValueError:
            base_amount = MINIMUM_BET
        return ConservativeStrategy(base_amount)
    else:
        return None

