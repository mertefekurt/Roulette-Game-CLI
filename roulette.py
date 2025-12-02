#!/usr/bin/env python3
import random

def spin_wheel():
    return random.randint(0, 36)

class Player:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
    
    def get_balance(self):
        return self.balance
    
    def add_balance(self, amount):
        self.balance += amount
    
    def subtract_balance(self, amount):
        self.balance -= amount

class Bet:
    def __init__(self, bet_type, value, amount):
        self.bet_type = bet_type
        self.value = value
        self.amount = amount

def main():
    print("welcome to roulette!")

if __name__ == "__main__":
    main()

