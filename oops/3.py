
#   NAME MANGLING

#__val__ is for special variables in python [dunder methods]
# underscores
# _ is for private variable
# var_ is for avoiding conflict with reserved keywords
# - is for unused variables
# __ is to hide the variable from outside the class


import datetime

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.transactions = []

    @staticmethod
    def current_time():
        return datetime.datetime.now()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append((amount, Account.current_time()))

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append((-amount, Account.current_time()))
        else:
            print("Insufficient balance or invalid amount.")

    def show(self):
        print(f"Account holder: {self.name}, Balance: {self.__balance}")

    def show_transac(self):
        for amount, date in self.transactions:
            if amount > 0:
                print(f"Account holder: {self.name}, \nDeposit: {amount} total balance: {self.__balance} \non {date} ")
            else:
                print(f"Account holder: {self.name}, total balance: {self.__balance} \nWithdrawal: {-amount} on {date} ")


# Testing
account1 = Account("Alice", 1000)
#account2 = Account("Bob", 500)
account1.__balance = 2000  

account1.deposit(200)
#account2.withdraw(100)

account1.show_transac()
#account2.show_transac()