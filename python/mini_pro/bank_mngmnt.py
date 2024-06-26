import json
class bank():
    def __init__(self):
        self.users = {}
        self.transaction_history = {}
        self.id_user = 0

    def save_to_file(self):
        try:
            data = {
                "users" : self.users,
                "transaction_history" : self.transaction_history,
                "id_user" : self.id_user
            }
            with open("../PYTHON/mini_pro/bank_data.json","w") as file:
                json.dump(data, file, indent=3)
            print("DATA SAVED SUCCESSFULLY TO THE FILE")
        except:
            print("AN ERROR OCCURED WHILE SAVE DATA TO FILE")

    def load_from_file(self):
        try:
            with open("../PYTHON/mini_pro/bank_data.json","r") as file:
                data = json.load(file)
                self.users = data.get("users", {})
                self.transaction_history = data.get("transaction_history", {})
                self.id_user = data.get("id_user", 0)
        except FileNotFoundError:
            print("NO EXISTING DATA")
        except:
            print("AN ERROR OCCURED WHILE LOAD DATA FROM FILE")

    def add_user(self, user_id, init_amount):
        self.id_user += 1
        user_id = str(self.id_user)
        if user_id not in self.users:
            if init_amount >= 500:
                self.users[user_id] = init_amount
                self.transaction_history[user_id] = []
                print(f"USER {user_id} ADDED WITH INITIAL AMOUNT ₹{init_amount}")
            else:
                print("YOU HAVE REQUIRED TO ADD MINIMUM ₹500 WHEN CREATING AN ACCOUNT")
        else:
            print(f"USER {user_id} ALREADY EXISTS.")
        self.save_to_file()

    def deposit_money(self, user_id, money):
        try:
            self.users[user_id] += money
            self.transaction_history[user_id].append(f"DEPOSITED ₹{money}") 
            print(f"DEPOSITED ₹{money} INTO USER {user_id} ACCOUNT. CURRENT BALANCE: ₹{self.users[user_id]}")
        except:
            print(f"USER {user_id} DOESN'T EXISTS.")
        self.save_to_file()
            
    def withdraw_money(self, user_id, money):
        try:
            if self.users[user_id] >= money:
                self.users[user_id] -= money
                self.transaction_history[user_id].append(f"WITHDRAWED ₹{money}")
                print(f"WITHDRAWED ₹{money} FROM USER {user_id} ACCOUNT. CURRENT BALANCE: ₹{self.users[user_id]}")
            else:
                print(f"INSUFFICIENT BALANCE FOR USER {user_id}")
        except:
            print(f"USER {user_id} DOESN'T EXISTS.")
        self.save_to_file()

    def check_transaction_history(self, user_id):
        try:
            if not self.transaction_history[user_id]:
                print(f"USER {user_id} HAS NO TRANSACTION HISTORY.")
            else:
                for transaction in self.transaction_history[user_id]:
                    print(transaction)
                balance = self.users[user_id]
                print(f"USER {user_id} CURRENT BALANCE IS ₹{balance}")
        except:
            print(f"USER {user_id} DOESN'T EXISTS.")

    def check_balance(self, user_id):
        try:
            balance = self.users[user_id]
            print(f"USER {user_id} CURRENT BALANCE IS ₹{balance}")
        except:
            print(f"USER {user_id} DOESN'T EXISTS.")

obj = bank()
obj.load_from_file()

while True:

    print("\n🏦----OM'S BANK MANAGEMENT SYSTEM----🏦")
    print("1.ADD USER🤴")
    print("2.DEPOSIT MONEY🤑")
    print("3.WITHDRAW MONEY💸")
    print("4.CHECK BALANCE🧾")
    print("5.CHECK TRANSACTION HISTORY☑️")
    print("6.EXIT🥲")

    number = int(input("ENTER YOUR CHOICE BETWEEN 1 TO 6: "))

    if number == 1:
        user_name = input("ENTER USER NAME: ")
        init_amount = float(input("ENTER AN INITIAL AMOUNT(MINIMUM ₹500): ₹"))
        obj.add_user(user_name, init_amount)

    elif number == 2:
        user_id = input("ENTER USER ID: ")  
        money = float(input("ENTER AMOUNT TO DEPOSIT: ₹"))
        obj.deposit_money(user_id, money)

    elif number == 3:
        user_id = input("ENTER USER ID: ")
        money = float(input("ENTER AMOUNT TO WITHDRAW: ₹"))
        obj.withdraw_money(user_id, money)

    elif number == 4:
        user_id = input("ENTER USER ID: ")
        obj.check_balance(user_id)

    elif number == 5:
        user_id = input("ENTER USER ID: ")
        obj.check_transaction_history(user_id)

    elif number == 6:
        obj.save_to_file()
        print("😊THANK YOU FOR USING OM'S BANK😊")
        break

    else:
        print("🙏PLEASE ENTER A NUMBER BETWEEN 1 TO 6🙏")
        
    dywtc = input("\nDO YOU WANT TO CONTINUE WITH OM'S BANK🤔 (Y/N):")
    if dywtc.lower() == 'n':
        obj.save_to_file()
        print("😊THANK YOU FOR USING OM'S BANK😊")
        break