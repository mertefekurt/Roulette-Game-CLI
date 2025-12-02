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

def check_color_bet(winning_number, bet_color):
    if winning_number == 0:
        return False
    return get_number_color(winning_number) == bet_color.lower()

def check_odd_even_bet(winning_number, bet_type):
    if winning_number == 0:
        return False
    if bet_type == "odd":
        return winning_number % 2 == 1
    else:
        return winning_number % 2 == 0

def check_high_low_bet(winning_number, bet_type):
    if winning_number == 0:
        return False
    if bet_type == "low":
        return 1 <= winning_number <= 18
    else:
        return 19 <= winning_number <= 36

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

def check_bet_win(bet, winning_number):
    if bet.bet_type == "number":
        return winning_number == bet.value
    elif bet.bet_type == "color":
        return check_color_bet(winning_number, bet.value)
    elif bet.bet_type == "odd" or bet.bet_type == "even":
        return check_odd_even_bet(winning_number, bet.bet_type)
    elif bet.bet_type == "high" or bet.bet_type == "low":
        return check_high_low_bet(winning_number, bet.bet_type)
    return False

def calculate_payout(bet, winning_number):
    if not check_bet_win(bet, winning_number):
        return 0
    
    if bet.bet_type == "number":
        return bet.amount * 36
    elif bet.bet_type in ["color", "odd", "even", "high", "low"]:
        return bet.amount * 2
    return 0

def main():
    print("welcome to roulette!")

if __name__ == "__main__":
    main()

