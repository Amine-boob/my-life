# project name : Digital Contact Book
# about this project : 
# is a program that manage all your phone numbers and their names .
# all the data will be saved on your desktop ,whenever you open the application
# you will find your data there . 
# you can add a number,delete a number,show all you stored numbers and search for a specific number by name .
# the structure :
# this project broken into three parts 
# 1- User class to deal with each user individually
# 2- ContactManager class manage each User class ,and used to fetch and deal with user's data ,
#    handle files,and handle log in/out
# 3- main function is the interface to interact with the user 

import pickle 
import bcrypt
import getpass
import os

class User :
    def __init__(self,phone_number,username,pin):
        self.phone_number = phone_number
        self.username = username 
        self.pin = pin  
        self.all_numbers = {}

    def add_decoration(func):
        def wrapper(*args,**kwargs):
            print("\n---------------------")
            func(*args,**kwargs)
            print("---------------------\n")
        return wrapper 
    
    #------ Contact management ------
    def add_contact(self,name,number):
        self.all_numbers.update({name:number})

    def delete_contact(self,name):
        self.all_numbers.pop(name,None)

    @add_decoration
    def get_contact_by_name(self,name):
        print(f"the   name    is    :{name}")
        print(f"the phone number is :{self.all_numbers.get(name)}")

    @add_decoration
    def show_contacts(self):
        if self.all_numbers :            
            for index,(key,value) in enumerate(self.all_numbers.items(),start=1):
                print(f"{index} - {key} : {value}")          
        else :
            print("you don't have any contact 📛")

    def get_list_of_contact_names(self):
        if self.all_numbers :
            return list(self.all_numbers.keys())
        else :
            return None  
    
    def verify_pin(self,mypin):
        byte_pin = mypin.encode("utf-8")
        if bcrypt.checkpw(byte_pin,self.pin):
            return True 
        else :
            return False 
    
class ContactManager :
    def __init__(self):
        self.path = os.path.expanduser("~/Desktop")
        self.path_to_contact_app = os.path.join(self.path,"Contact Book.pkl")
        self.all_users = []
        self.current_number = ""
        self.current_user = ""
    
    # ------ handle user data ------
    def get_user_data(self,number): # get data based on the phone number
        for user in self.all_users :
            if user.phone_number == number :
                return user 
        return None
    def get_all_numbers(self):
        if len(self.all_users) != 0 :
            numbers = []
            for number in self.all_users :
                numbers.append(number.phone_number)
            return numbers
        else :
            return []
    def get_all_usernames(self):
        if len(self.all_users) != 0 :
            names = []
            for name in self.all_users :
                names.append(name.username)
            return names 
        else :
            return []
    
    # ------ file handling -------
    def get_data_from_file(self):
        try : 
            with open(self.path_to_contact_app , "rb") as file :
                data = pickle.load(file)
                self.all_users = data
        except FileNotFoundError :
            with open(self.path_to_contact_app ,"wb") as file :
                pickle.dump([],file)
    def add_data_to_file(self):
        with open(self.path_to_contact_app ,"wb") as file :
            pickle.dump(self.all_users,file)
    def save_changes(self) :
        self.add_data_to_file()


    def hash_function(self,pwd):
        byte_pwd = pwd.encode("utf-8")
        return bcrypt.hashpw(byte_pwd,bcrypt.gensalt(rounds=14))
    
    # ------ file log in/out -------
    def log_in(self):
        while True :
                number = input("enter your number (+212 *** *** ***) (q to quit):").strip()
                if number == "q":
                    print("try again later 📛")
                    return 
                elif "+" not in number :
                    print("incorrect password ,print the correct formula !!📛")
                    continue 
                elif number.count(" ") != 3 :
                    print("incorrect password ,print the correct formula !!📛")
                    continue 
                elif len(number) != 16 :
                    print("incorrect password ,print the correct formula !!📛")
                    continue
                else :
                    print("correct phone number !✅")
                    break  
               
        if number in self.get_all_numbers() : #you need to verify the account
            print("you already have an account ✅") 
            userdata = self.get_user_data(number)
            pin_attempt = 2
            while True :
                pin = getpass.getpass("verify your pin (q to quit):")
                if pin == "q":
                    print("try again later 📛")
                    return 
                elif userdata.verify_pin(pin) :
                    self.current_number = number 
                    self.current_user = userdata.username
                    print("correct pin ✅")
                    break
                elif pin_attempt > 0 :
                    print(f"incorrect pin, you have {pin_attempt} attempt 📛")
                    pin_attempt -= 1
                else :
                    print("try again later !📛")
                    return 

        else : # set a pin ,set a username,and add data to file 📛✅
            while True :
                pin = getpass.getpass("set a pin using 4 digits (q to quit):")
                if pin == "q":
                    print("try again later 📛")
                    return 
                elif not pin.isdigit():
                    print("enter just digits 📛")
                elif pin == "":
                    print("enter something !📛")
                elif len(pin) != 4 :
                    print("enter a password from 4 digits📛")
                else :   
                    print("valid pin ✅")                                       
                    break
            while True :
                username = input("set a username (q to quit):")
                if username == "q":
                    print("try again later 📛")
                    return 
                elif username == "":
                    print("enter something 📛")
                elif username in self.get_all_usernames():
                    print("username already exist, pick another one 📛")
                else :
                    hash = self.hash_function(pin)
                    self.all_users.append(User(number,username,hash))
                    self.current_number = number 
                    self.current_user = username 
                    self.save_changes()
                    print("account created ✅")
                    break 
    def log_out(self):
        if not self.current_number :
            print("you are already logged out 📛")
        else :
            self.current_number = ""
            self.current_user = ""
            print("you successfully logged out ✅")  

def main():
    application = ContactManager()
    is_running = True 
    application.get_data_from_file()
    while is_running :
        if application.current_number :
            user_data = application.get_user_data(application.current_number)
        else :
            pass
        print("----- Contact Book ----- ")
        print(f"Hello {application.current_user}")
        print("--------------------------")
        print("1 - confirm your phone number ")
        print("2 - log out")
        print("3 - show my contact ")
        print("4 - search for a number by name ")
        print("5 - add contact")
        print("6 - delete contact")
        print("7 - quit")
        print("-------------------------")
        choice = input("enter your choice :")
        if choice == "1":
            application.log_in()
        elif choice == "2":
            application.log_out()
        elif choice == "3":
            if application.current_number :
                user_data.show_contacts()
            else :
                print("you need to log in first 📛")
        elif choice == "4":
            if application.current_number :
                data = user_data.get_list_of_contact_names() # to get a list contain all my contacts of they exist
                if data : #to check if there's any contact
                    while True :
                        name = input("enter the name (q to quit):")
                        if name == "q":
                            print("try again later")
                            break 
                        elif name not in data :
                            print("this name not found 📛")
                        else :
                            user_data.get_contact_by_name(name)
                            break 
                else :
                    print("you don't have any contact 📛")                   
            else :
                print("you need to log in first 📛")
        elif choice == "5":
            if application.current_number :
                while True :
                    name = input("enter the name :")
                    if name == "":
                        print("enter something 📛")
                    else :
                        break 
                while True :
                    number = input("enter the number :")
                    if number == "":
                        print("enter something 📛")
                    else : 
                        user_data.add_contact(name,number)
                        application.save_changes()
                        print(f"you successfully added '{name}' to you contact book✅")
                        break 
            else :
                print("you need to log in first 📛")
        elif choice == "6":
            if application.current_number :
                data = user_data.get_list_of_contact_names() # to get a list contain all my contacts of they exist
                if data : #to check if there's any contact
                    while True :
                        name = input("enter the name (q to quit):")
                        if name == "q":
                            print("try again later")
                            break 
                        elif name not in data :
                            print("this name not found 📛")
                        else :
                            user_data.delete_contact(name)
                            print(f"you successfully delete '{name}' from your contact book✅")
                            break
                else :
                    print("you don't have any contact 📛")
            else :
                print("you need to log in first 📛")
        elif choice == "7":
            is_running =False
        
        else :
            print("invalid input")


if __name__=='__main__':
    main()
