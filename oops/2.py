import datetime

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    @staticmethod #static method is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, 
    #        rather than on an instance of the class.
    def current_time():
        return datetime.datetime.now()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((amount, Account.current_time()))

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append((-amount, Account.current_time()))
        else:
            print("Insufficient balance or invalid amount.")

    def show(self):
        print(f"Account holder: {self.name}, Balance: {self.balance}")

    def show_transac(self):
        for amount, date in self.transactions:
            if amount > 0:
                print(f"Account holder: {self.name}, Deposit: {amount} on {date}")
            else:
                print(f"Account holder: {self.name}, Withdrawal: {-amount} on {date}")


# Testing
account1 = Account("Alice", 1000)
account2 = Account("Bob", 500)

account1.deposit(200)
account2.withdraw(100)

account1.show_transac()
account2.show_transac()