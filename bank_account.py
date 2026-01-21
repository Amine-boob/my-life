# bank account
def show_balance(balance):
    print(f"you have in your account ${balance:.2f}")
def deposit():
    amount = float(input("enter an amount to deposited"))
    if amount <0 :
        print("enter just positive numbers :")
        return 0
    else :
        return amount
def with_draw(balance):
    drawn = float(input("enter a number to drow :"))

    if drawn > balance :
        print("that not invalid ,you don't have this number in your account ")
        return 0
    elif drawn <0 :
        print("you can't draw a negative number")
        return 0
    else :
        return drawn
def main():
    balance = 0
    isrunning = True

    while isrunning :
        print("-------------")
        print("bank program ")
        print("-------------")
        print("1.to show balance")
        print("2.to deposit an amount ")
        print("3.with draw ")
        print("4.quit")
        print("-------------")
        choice = input("enter your choice (1-4) :")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= with_draw(balance)
        elif choice == "4":
            isrunning = False
        else:
            print("your choice invalid !!")
    print("have a good day")

if __name__ == '__main__':
    main()








# this time working with class 

class Banc :
    def __init__(self):
        self.balance = 0

    def show_balance(self):
        print(f"you have in your account ${self.balance:.2f}")

    def deposit(self):
        amount = input("enter an amount to deposited")
        if amount.isdigit():
            amount = float(amount)
            if amount <= 0:
                print("you can't deposit negative number or zero 📛")

            else :
                 self.balance += amount
        else:
            print("enter just digits 📛")

    def withdraw(self):
        amount = input("enter a number to drow :")
        if amount.isdigit():
            amount = float(amount)
            if amount > self.balance:
                print("you don't have this amount 📛")

            elif amount <= 0:
                print("you can't withdraw a negative number or zero 📛")

            else:
                self.balance -= amount
        else:
            print("enter just digits 📛")


def main():
    user = Banc()
    is_running = True
    while is_running :
        print("-------------")
        print("bank program ")
        print("-------------")
        print("1.to show balance")
        print("2.to deposit an amount ")
        print("3.with draw ")
        print("4.quit")
        print("-------------")
        choice = input("enter your choice (1-4) :")
        if choice == "1":
            user.show_balance()
        elif choice == "2":
            user.deposit()
        elif choice == "3":
            user.withdraw()
        elif choice == "4":
            is_running = False
        else:
            print("your choice invalid !! 📛")
    print("have a good day")

if __name__ == '__main__':
    main()
