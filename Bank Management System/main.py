'''
Create Account
Deposit Money
Withdraw Money
Check Balance
Transfer Money (Bonus)
'''

accounts = []
import random


class BankAccount:

    def __init__(self,account_name, account_number, initial_balance):
        self.account_name = account_name
        self.account_number = account_number
        self.initial_balance = initial_balance

    def account(self):
        print(f"Name: {self.account_name}")
        print(f"Account No: {self.account_number}")
        print(f"Balance: {self.initial_balance}")
        print("-" * 25)

    def deposit(self, depositt):
        self.initial_balance += depositt
        print(f"You deposited {depositt} money and your current balance is {self.initial_balance}")

    def withdraw(self, amount):        

        if self.initial_balance >= amount:
            self.initial_balance -= amount
            print(f"{amount} has been credited from {self.account_number} account number. Your remaining balance is {self.initial_balance}")
        else:
            print("You don't have enough balance")

    def check_balance(self):
        print(f"Your current balance is {self.initial_balance}")

# account1 = BankAccount("Harshu", "19191", 1000)
# account1.account()
# account1.deposit(500)
# account1.withdraw(200)
# account1.check_balance()

while True:

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    user = input("Choose an option: ")

    if user == "1":
        acc_name = input("Enter your name: ")
        acc_no = random.randint(10000, 99999)
        acc_bal = int(input("Enter the initial amount: "))
        consumer = BankAccount(acc_name,acc_no,acc_bal)
        accounts.append(consumer)

        print(f"Account created Succesfully ✅ and your account number is {acc_no}")

    elif user == "2":
        number = input("Enter your account number: ")
        depo = int(input("Enter the amount you want to deposit: "))

        for consumer in accounts:
            if consumer.account_number == number:
                consumer.deposit(depo)
                break
            else:
                print("Account not found ❌")

    elif user == "3":
        number = input("Enter your account number: ")
        draw = int(input("Enter the amount you want to withdraw: "))

        for consumer in accounts:
            if consumer.account_number == number:
                consumer.withdraw(draw)
                break
            else:
                print("Account not found ❌")


    elif user == "4":
        number = input("Enter your account number: ")

        for consumer in accounts:
            if consumer.account_number == number:
                consumer.check_balance()
                break
            else:
                print("Account not found ❌")
        

    elif user == "5":
        number = input("Enter your account number: ")
        ("\n")
        found = False
        for consumer in accounts:
            if consumer.account_number == number:
                consumer.account()
                found = True
                break
        if not found:
            print("Account not found ❌")

    elif user == "6":
        print("Thanks for visiting 😊")
        break
    else:
        print("Choose a valid option between (1-6)")