# from datetime import date

# today = date.today() 
# print("Date:",today)  #return today's date 
# print("Current year:", today.year)  #return current year
# print("Current month:", today.month) #return current month
# print("Current day:", today.day) #return current day

# class BankManagementSystem:
#     def __init__(self):
#         self.users = {}

#     def add_user(self, user_id, initial_balance=0):
#         if user_id not in self.users:
#             self.users[user_id] = initial_balance
#             print(f"User {user_id} added successfully with an initial balance of ${initial_balance}")
#         else:
#             print(f"User {user_id} already exists!")

#     def deposit_money(self, user_id, amount):
#         if user_id in self.users:
#             self.users[user_id] += amount
#             print(f"Deposited ${amount} successfully. New balance: ${self.users[user_id]}")
#         else:
#             print(f"User {user_id} does not exist!")

#     def check_balance(self, user_id):
#         if user_id in self.users:
#             print(f"Balance for user {user_id}: ${self.users[user_id]}")
#         else:
#             print(f"User {user_id} does not exist!")

#     def withdraw_money(self, user_id, amount):
#         if user_id in self.users:
#             if amount <= self.users[user_id]:
#                 self.users[user_id] -= amount
#                 print(f"Withdrew ${amount} successfully. New balance: ${self.users[user_id]}")
#             else:
#                 print(f"Insufficient funds for user {user_id}")
#         else:
#             print(f"User {user_id} does not exist!")

#     def bank_statement(self, user_id):
#         if user_id in self.users:
#             print(f"Bank statement for user {user_id}:")
#             print(f"Balance: ${self.users[user_id]}")
#         else:
#             print(f"User {user_id} does not exist!")

# def main():
#     bank = BankManagementSystem()

#     while True:
#         print("\nBank Management System Menu:")
#         print("1. Add User")
#         print("2. Deposit Money")
#         print("3. Check Balance")
#         print("4. Withdraw Money")
#         print("5. Bank Statement")
#         print("6. Quit")

#         choice = input("Enter your choice (1-6): ")

#         if choice == "1":
#             user_id = input("Enter user ID: ")
#             initial_balance = float(input("Enter initial balance: "))
#             bank.add_user(user_id, initial_balance)
#         elif choice == "2":
#             user_id = input("Enter user ID: ")
#             amount = float(input("Enter amount to deposit: "))
#             bank.deposit_money(user_id, amount)
#         elif choice == "3":
#             user_id = input("Enter user ID: ")
#             bank.check_balance(user_id)
#         elif choice == "4":
#             user_id = input("Enter user ID: ")
#             amount = float(input("Enter amount to withdraw: "))
#             bank.withdraw_money(user_id, amount)
#         elif choice == "5":
#             user_id = input("Enter user ID: ")
#             bank.bank_statement(user_id)
#         elif choice == "6":
#             print("Exiting Bank Management System. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 6.")

#         choice = input("Do you want to continue? (y/n): ")
#         if choice.lower() == "n":
#             break

# if __name__ == "__main__":
#     main()

class Bank:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, initial_balance=0):
        if user_id not in self.users:
            if initial_balance >= 500:
                self.users[user_id] = initial_balance
                print(f"User {user_id} added successfully with initial balance {initial_balance}")
            else:
                print("Initial balance must be at least 500.")
        else:
            print(f"User {user_id} already exists!")

    def deposit(self, user_id, amount):
        try:
            self.users[user_id] += amount
            print(f"Deposited {amount} into user {user_id}'s account. Current balance: {self.users[user_id]}")
        except KeyError:
            print(f"User {user_id} does not exist!")

    def withdraw(self, user_id, amount):
        try:
            if self.users[user_id] >= amount:
                self.users[user_id] -= amount
                print(f"Withdrew {amount} from user {user_id}'s account. Current balance: {self.users[user_id]}")
            else:
                print(f"Insufficient funds for user {user_id}")
        except KeyError:
            print(f"User {user_id} does not exist!")

    def check_statement(self, user_id):
        try:
            balance = self.users[user_id]
            print(f"User {user_id}'s current balance: {balance}")
        except KeyError:
            print(f"User {user_id} does not exist!")

# Main program
bank = Bank()

while True:
    print("\n===== Bank Management System =====")
    print("1. Add User")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Statement")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        user_id = input("Enter user ID: ")
        initial_balance = float(input("Enter initial balance (minimum 500): "))
        bank.add_user(user_id, initial_balance)

    elif choice == '2':
        user_id = input("Enter user ID: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(user_id, amount)

    elif choice == '3':
        user_id = input("Enter user ID: ")
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(user_id, amount)

    elif choice == '4':
        user_id = input("Enter user ID: ")
        bank.check_statement(user_id)

    elif choice == '5':
        print("Exiting the Bank Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

    continue_choice = input("Do you want to continue? (y/n): ")
    if continue_choice.lower() != 'y':
        print("Exiting the Bank Management System. Goodbye!")
        break


class Bank:
    def __init__(self):
        self.users = {}
        self.transaction_history = {}

    def add_user(self, user_id, initial_balance=0):
        if user_id not in self.users:
            if initial_balance >= 500:
                self.users[user_id] = initial_balance
                self.transaction_history[user_id] = []
                print(f"User {user_id} added successfully with initial balance {initial_balance}")
            else:
                print("Initial balance must be at least 500.")
        else:
            print(f"User {user_id} already exists!")

    def deposit(self, user_id, amount):
        try:
            self.users[user_id] += amount
            self.transaction_history[user_id].append(f"Deposited {amount}")
            print(f"Deposited {amount} into user {user_id}'s account. Current balance: {self.users[user_id]}")
        except KeyError:
            print(f"User {user_id} does not exist!")

    def withdraw(self, user_id, amount):
        try:
            if self.users[user_id] >= amount:
                self.users[user_id] -= amount
                self.transaction_history[user_id].append(f"Withdrew {amount}")
                print(f"Withdrew {amount} from user {user_id}'s account. Current balance: {self.users[user_id]}")
            else:
                print(f"Insufficient funds for user {user_id}")
        except KeyError:
            print(f"User {user_id} does not exist!")

    def check_statement(self, user_id):
        try:
            balance = self.users[user_id]
            print(f"User {user_id}'s current balance: {balance}")
            print(f"Transaction History for user {user_id}:")
            for transaction in self.transaction_history[user_id]:
                print(transaction)
        except KeyError:
            print(f"User {user_id} does not exist!")

# Rest of your code remains unchanged...
