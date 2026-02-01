# bank simulator
class User :
    def __init__(self,username,password,balance):
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def verify_password(self,check):
        if check == self.password :
            return True
        else :
            return False
    def change_password(self):
        pass

class Bank :
    def __init__(self):
        self.all_users = [User("amine","123456",0)]
        self.current_user = ""

    def get_user_data(self,text):
        for user in self.all_users :
            if user.username == text :
                return user
        return None

    def all_users_list(self):
        names = []
        for user in self.all_users :
            names.append(user.username)
        return names

    def create_account(self):
        is_running = True
        while is_running:
            get_name = input("enter your username (q to quit):")
            if get_name == "":
                print("enter something 📛")
                continue
            if get_name == "q" or get_name == "Q":
                return
            if get_name in self.all_users_list() :
                print("user name exist choose another one 📛")
                continue
            else :
                is_running = False
        out = True
        while out:
            pwd = input("enter your password :")
            if pwd == "":
                print("you didn't enter anything 📛")
            else:
                self.all_users.append(User(get_name, pwd, 0))
                self.current_user = get_name
                print("account created ✅")
                out = False

    def log_in(self):
        is_run = True
        while is_run :
            name = input("enter your username (q to quit):")
            if name == "" :
                print("enter something 📛")
                continue
            if name == "q" :
                return
            elif name in self.all_users_list() :
                print("account found ✅")
                is_run = False
        is_running = True
        password_attempt = 2
        while is_running :
            pwd = input("enter your password :")
            if self.get_user_data(name).verify_password(pwd) : # True
                print("password correct ✅")
                self.current_user = name
                is_running = False
            elif password_attempt >0 :
                print("password incorrect ")
                print(f"you have {password_attempt} left !!")
                password_attempt -= 1
            else :
                print("try again later")
                return

def main():
    program = Bank()
    is_running = True
    while is_running :
        print("----- bank program -----")
        print(f" hello {program.current_user}")
        print("-------------------------")
        print("1 - create account")
        print("2 - log in ")
        print("3 - show balance ")
        print("4 - deposit")
        print("5 - withdraw")
        print("6 - quit")
        print("------------------------")
        choice = input("enter your choice :")
        if choice == "1" :
            program.create_account()
        elif choice =="2":
            program.log_in()
        elif choice == "3":
            if program.get_user_data(program.current_user) :
                user_data = program.get_user_data(program.current_user)
                print("\n------------ your balance -------------")
                print(f"your current balance is : {user_data.balance:.2f}$")
                print("---------------------------------------\n")
            else :
                print("you are logged out, you need to log in first 📛")
        elif choice == "4":
            if program.get_user_data(program.current_user) :
                user_data = program.get_user_data(program.current_user)
                is_run = True
                while is_run:
                    try:
                        amount = int(input("enter your amount :"))
                        if amount <= 0:
                            print("you can't deposit negative number or the zero 📛")
                        else:
                            user_data.deposit(amount)
                            print(f"you successfully deposit an amount of : {amount:.2f}$ ✅")
                            is_run = False
                    except ValueError:
                        print("enter just digits 📛")
            else :
                print("you are logged out, you need to log in first 📛")

        elif choice == "5":
            if program.get_user_data(program.current_user) :
                user_data = program.get_user_data(program.current_user)
                out = True
                while out:
                    try:
                        amount = int(input("enter your amount :"))
                        if amount <= 0:
                            print("amount can't be negative 📛")
                        elif amount > user_data.balance :
                            print("you don't have this amount 📛")
                        else:
                            user_data.withdraw(amount)
                            print(f"you successfully withdraw an amount of : {amount:.2f}$ ✅")
                            out = False
                    except ValueError:
                        print("enter just digits 📛")
            else :
                print("you are logged out, you need to log in first 📛")

        elif choice == "6":
            print("goodbye , visit us later ")
            is_running = False
        else :
            print("📛invalid input📛")

if __name__=='__main__':
    main()

#Account (balance, deposit, withdraw)

#User (owns accounts)

#Bank (creates accounts, transfers money)
