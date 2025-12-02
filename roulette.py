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

