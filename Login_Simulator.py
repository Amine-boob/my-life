# Password Verification System (Login Simulator)

# the next level :
#hashing → later bcrypt / argon2
#file DB → later real databases
#username validation → later regex

# this project cover :
#✅ Registration
#✅ Login
#✅ Password strength validation
#✅ Password confirmation
#✅ Salted hashing
#✅ File-based “database”
#✅ Password verification
#✅ Password change feature
#✅ File rewrite using r+, seek, truncate
#✅ Error handling
#✅ Separation into many functions

import hashlib
import secrets
import string
import getpass
import sys
def send_data_to_database(username,salt_value,hash_password):
    # let create a file and pretend it is a database
    path = "Database"

    with open(path ,"a") as file :
        file.write(f"{username}:{salt_value}:{hash_password}\n")
        print("Your register are successfully accepted ")


def get_user_data(username):
    path = "Database"
    try :
        with open(path , "r") as file :
            data = file.readlines()
            for line in data :
                stored_username = line.split(":")[0]
                if username ==stored_username:
                    return line.strip()
            return None
    except FileNotFoundError:
        print("error 500 ,try again later")
        print("there is a problem from the server side")
        return False

def get_password() :
    numbers = string.digits
    punctuation = string.punctuation
    is_running = True
    while is_running :
        count_number = 0
        count_punctuation = 0
        attempt = 3
        my_password = getpass.getpass("Enter your password for the first time :")

        if len(my_password) <8 :
            print("📛Weak password📛,your password too short ")
            continue
        for ch in my_password :
            if ch in numbers :
                count_number += 1
            elif ch in punctuation :
                count_punctuation += 1

        if count_number < 2 :
            print("📛Weak password📛,enter at least 2 digits ")
            continue
        if count_punctuation < 1 :
            print("📛Weak password📛,enter at least one special character")
            continue

        while attempt > 0 :
            print(f"Enter the password again,you have {attempt} to repeat your previous password :")
            pwd_again = getpass.getpass("enter your password for the second time :")
            if pwd_again == my_password :
                print("nice work , your password is strong 👍🏼 and valid ✅ ")
                return my_password
            else :
                attempt -=1
        if attempt == 0 :
            print("fail ,try again !")

    return None

def get_salt():
    numbers = str(string.digits+string.ascii_letters)
    salt = ""
    for ch in range(10):
        salt += secrets.choice(numbers)
    return salt

def inside_the_application(name):
    user_data = get_user_data(name)
    while True  :
        print("\n----------------------------------")
        print("You are now inside the application ")
        print("----------------------------------\n")
        print(f"welcome {name}\n")
        print("1 - return to the main menu")
        print("2 - quit the application ")
        print("3 - change the password ")
        number = input("enter your choice :")
        if number == "1" :
            break
        elif number == "2":
            sys.exit()
        elif number == "3" :
            password_attempt = 2
            while True :
                verify_your_pwd = getpass.getpass("verify your password :")
                user_da = check_password(user_data,verify_your_pwd)
                if user_da : # it return true if the password correct
                    print("password correct 👍🏼")
                    print("choose another password :")
                    new_password = get_password()
                    new_salt = get_salt()
                    new_password_hash = hashing_function(new_password,new_salt)
                    modify = modify_password(name,new_password_hash,new_salt)
                    if modify :
                        print("password changed ✅✨")
                        break
                    else :
                        break
                elif password_attempt > 0:
                    print("password incorrect ❌")
                    print(f"you have {password_attempt} attempt left")
                    password_attempt -= 1

                elif not user_da :
                    print("something went wrong ,try again later")
                    break
        else:
            print("📛invalid input 📛")

def modify_password(name,new_password_hash,new_salt):
    try :
        with open("Database", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for line in lines:
                if line.startswith(name):
                    file.write(f"{name}:{new_salt}:{new_password_hash}\n")
                else:
                    file.write(line)
        return True
    except FileNotFoundError :
        print("error 500 ,try again later")
        print("there is a problem from the server side")
        return False

def check_password(user_data,user_password) :
    split_data = user_data.split(":")
    make_hash_to_test = user_password + split_data[1]
    make_hash = hashlib.sha3_512(make_hash_to_test.encode()).hexdigest()
    if make_hash == split_data[2] :
        return True
    else :
        return False

def hashing_function(password,salt_value) :
    full_password = password + salt_value
    return hashlib.sha3_512(full_password.encode()).hexdigest()

def main():
    is_running = True
    while is_running :
        print("******** bank ********")
        print("1 - register")
        print("2 - log in ")
        print("3 - quit")
        print("**********************")
        choice = input("Enter a number 1 -> 3 :")
        if choice == "1":
            print("\n-----------------------")
            print("---- register page ----")
            print("-----------------------\n")

            while True :
                username = input("create a username (q to quit):")
                check_if_user_name_exist = get_user_data(username)
                if username=="q" or username=="Q" :
                    break
                else:
                    if not check_if_user_name_exist :
                        password = get_password()
                        salt_value = get_salt()
                        hash_password = hashing_function(password,salt_value)
                        send_data_to_database(username,salt_value,hash_password)
                        inside_the_application(username)
                        break
                    else :
                        print("📛username already token 📛,choose another username ")

        elif choice == "2" :
            print("\n-----------------------")
            print("------ log in page ------")
            print("-----------------------\n")
            enter_user_attempt = 2
            while True :
                username = input("enter your user name :")
                user_data = get_user_data(username)
                if user_data == False :
                    break
                if user_data:
                    print("user name found ")
                    break
                elif enter_user_attempt >0 :
                    print("user name not found ")
                    print(f"you have {enter_user_attempt} to enter your user name")
                    enter_user_attempt -= 1
                elif enter_user_attempt == 0 :
                    print("Fail to log in ❌,try again later ")
                    break
            if user_data :
                enter_password_attempt = 2
                while True :
                    user_password = getpass.getpass("enter your password :")
                    true_or_false = check_password(user_data,user_password)
                    if true_or_false :
                        print("Access granted ✅")
                        inside_the_application(username)
                        break
                    elif not true_or_false and enter_password_attempt >0:
                        print("Access denied ❌")
                        print(f"you have {enter_password_attempt} attempt to enter your password")
                        enter_password_attempt -= 1
                    elif enter_password_attempt == 0 :
                        print("Fail to log in ❌,try again later ")
                        print("password incorrect ")
                        break
            else :
                continue
        elif choice == "3":
            is_running = False
            print("goodbye\nvisit us later")
        else :
            print("📛invalid input📛")

if __name__ == '__main__' :
    main()

#Access granted
#Access denied
