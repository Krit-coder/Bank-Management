class Bank:
    no_of_customer = 0
    account_number = 11034570

    def __init__(self, name, mobile_number, opening_balance, pin):
        self.name = name
        self.mobile_number = mobile_number
        self.customer_account_number = Bank.account_number
        self.pin = pin
        self.balance = opening_balance

        Bank.account_number += 1
        Bank.no_of_customer += 1

    def basic_details(self):
        print(
            f"Name : {self.name}\nAccount Number : {self.customer_account_number}\nBalance : Rs.{self.balance}")

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(
                f"Transaction Completed.\nCurrent Balance : Rs.{self.balance}")
        else:
            print("Invalid amount.\nTransaction Aborted")

    def withdrawl(self):
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(
                f"Transaction Completed.\nCurrent Balance : Rs.{self.balance}")
        else:
            print("Invalid amount.\nTransaction Aborted")

    def payment(self, other):
        amount = int(input("Enter the amount to pay: "))
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            other.balance += amount
            print(
                f"Transaction Completed.\nCurrent Balance : Rs.{self.balance}")
        else:
            print("Invalid amount.\nTransaction Aborted")
