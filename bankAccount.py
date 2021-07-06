from random import randint
import sys
sys.path.append(".")
from User import *


class BankAccount:
    def __init__(self, username, int_rate=5, balance=0):
        self.name = username
        self.int_rate = int_rate
        self.account_balance = balance
		
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def yield_interest(self,t):
        print("The principal is", self.account_balance)
        print("The time period is", t, "months")
        print("The rate of interest is", self.int_rate)
        si = (self.account_balance*t*self.int_rate)/100
        print("The Simple Interest is", si)
        return si

Account1 = BankAccount("User1", 5, 150)
Account2 = BankAccount("User2", 5, 225)

Account1.make_deposit(200).make_deposit(250).make_deposit(125).make_withdrawal(80).yield_interest(4)
print('\n')
Account2.make_deposit(55).make_deposit(150).make_withdrawal(40).make_withdrawal(40).make_withdrawal(40).make_withdrawal(40).yield_interest(4)

# when I try to chain .display_account_info() to the end it keeps giving me a "float" error so I took it off 