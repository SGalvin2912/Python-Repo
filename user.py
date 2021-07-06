from random import randint
import sys
sys.path.append(".")
from BankAccount import *


class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.BankAccount = BankAccount

    def make_deposit(self, amount):
        self.BankAccount += amount
        return self

    def make_withdrawal(self, amount):
        self.BankAccount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

Sean = User("Sean Galvin", "bsemail2912@gmail.com")
Kelly = User("Kelly Galvin", "kellyemail@gmail.com")
Rox = User("Roxanne Lambden", "roxemail@email.com")

Sean.make_deposit(500).make_deposit(300).make_deposit(200).make_withdrawal(75).display_user_balance()
Kelly.make_deposit(700).make_deposit(1000).make_withdrawal(50).make_withdrawal(75).display_user_balance()
Rox.make_deposit(2000).make_withdrawal(55).make_withdrawal(55).make_withdrawal(55).display_user_balance()