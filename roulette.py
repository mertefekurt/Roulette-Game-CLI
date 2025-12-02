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

def main():
    print("welcome to roulette!")

if __name__ == "__main__":
    main()

