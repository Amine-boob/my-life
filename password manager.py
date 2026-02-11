# Simple Password Manager
class Credential :
    def __init__(self,service_name,username,password) :
        self.service_name = service_name
        self.username= username
        self.password = password
        #return masked password (e.g. ********) ✅
        #return full password (only when requested)

    def mask_password(self):
        return "*"*len(self.password)

class User :
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.vault = {}

    def list_service(self):
        print("\n----- your services -----")
        for index,key in enumerate(self.vault.keys() ,start=1) :
            print(f"{index} - {key} ")
        print("-------------------------\n")

    def list_of_services(self):
        #return list(self.vault.keys())
        services = []
        for key in self.vault.keys() :
            services.append(key)
        return services

    def verify_password(self,check):
        if check == self.password :
            return True
        else :
            return False

    def add_credential(self,service_name,username,password):
        self.vault.update({service_name:Credential(service_name,username,password)})

    def get_credential_by_service(self,data):      
        the_data = self.vault.get(data)
        if not the_data :
            print("Service not found 📛")
            return 
        print("\n-------- Data --------")
        print(f"service name : {the_data.service_name}")
        print(f"username : {the_data.username}")
        print(f"your password : {the_data.mask_password()}")
        print("---------------------\n")

    def get_password_when_requested(self,data) :
        the_data = self.vault.get(data)
        print("\n------- the password --------")
        print("keep this password secret!") 
        print(f"your password : {the_data.password}")
        print("------------------------------\n")

    def delete_credential(self,data) :
        self.vault.pop(data)

        #add_credential ✅
        #delete credential ✅
        #get credential  by  service ✅
        #list services ✅


class PasswordManager :
    def __init__(self):
        self.all_users = []
        self.current_user = ""

    def get_user_data(self,current):
        for user in self.all_users :
            if user.username == current :
                return user
        return None

    def all_names(self):
        names = []
        for user in self.all_users :
            names.append(user.username)
        return names

    def create_user(self):
        is_run = True
        while is_run :
            name = input("enter your username (q to quit):")
            if name == "":
                print("enter something 📛")
            elif len(name)< 6 :
                print("username too short!!\ntry another one more then 6 character 📛")
            elif name == "q":
                return
            else :
                print("username valid ✅")
                is_run = False  
        is_running = True
        while is_running :
            pwd = input("enter your password (q to quit):")
            if pwd == "" :
                print("enter something 📛")
            elif pwd == "q":
                return
            else :
                self.all_users.append(User(name,pwd))
                self.current_user = name
                print("account created ✅")
                is_running = False

    def log_in(self):
        while True :
            name = input("enter your username (q to quit):")
            if name == "":
                print("enter something 📛")
            elif name == "q":
                print("try again later !!")
                return
            elif name in self.all_names() :
                print("username correct ✅")
                break
            else :
                print("user not found 📛")
        pwd_attempt = 2
        while True :
            pwd = input("enter your password (q to quit):")
            if pwd == "q" :
                print("try again later !!")
                return
            if self.get_user_data(name).verify_password(pwd) :
                self.current_user = name
                print("password correct ✅")
                break
            elif pwd_attempt > 0 :
                print(f"incorrect password 📛,you have {pwd_attempt}")
                pwd_attempt -= 1
            else :
                print("try again later !!")
                break

    def log_out(self):
        if self.current_user :
            self.current_user = ""
            print("you successfully logged out ✅")
        else :
            print("you are already logged out 📛")

        #create account ✅
        #log in ✅
        #log out ✅
        #route commands to the active user

def main():
    me = PasswordManager()
    is_running = True
    while is_running :
        user_data = None
        if me.current_user :
            user_data = me.get_user_data(me.current_user)
        else :
            pass 
        print("---- password manager ----")
        print(f"Hello {me.current_user}")
        print("--------------------------")
        print("1 - create an account")
        print("2 - log in")
        print("3 - log out ")
        print("4 - view stored services")
        print("5 - add credential ")
        print("6 - retrieve all data about a service")
        print("7 - delete service")
        print("8 - quit")
        print("---------------------------")
        choice = input("enter your choice :")
        if choice == "1":
            me.create_user()
        elif choice =="2" :
            me.log_in()
        elif choice =="3" :
            me.log_out()
        elif choice =="4" :
            # check if the user loged in 
            if me.current_user :
                # check if there is a crential first :
                if len(user_data.list_of_services()) != 0 :
                    user_data.list_service()
                else :
                    print("you don't have any credential")
            else :
                print("you need to log in first 📛")
        elif choice =="5" :
            if me.current_user :
                #service name :
                while True :
                    service_name = input("enter the name of that service :")
                    if service_name in user_data.list_of_services() :
                        print("this service already exist 📛")
                        continue
                    if service_name == "":
                        print("you need to enter something 📛")
                    else :
                        break
                # username :
                while True :
                    username = input("enter your username :")
                    if username == "":
                        print("you need to enter something 📛")
                    else:
                        break
                # password
                while True :
                    password = input("enter your password :")
                    if password == "":
                        print("you need to enter something 📛")
                    else:
                        # add this data
                        user_data.add_credential(service_name, username, password)
                        print("data successfully added ✅")
                        break
            else :
                print("you need to log in first 📛")
        elif choice =="6" :
            if me.current_user :
                length = len(user_data.list_of_services())
                if length != 0 :
                    while True :
                        
                        number = input(f"enter the number of that service :")
                        if number.isdigit() :
                            number = int(number)
                            if not 1 <= number <= length :
                                print("your number out of range 📛")
                            else :
                                get_service_name = user_data.list_of_services()[number -1]
                                user_data.get_credential_by_service(get_service_name)
                                break
                        else :
                            print("enter a number 📛")
                    while True :
                        get_password = input("do you want to show the password of that service (Y/N):").upper()
                        if get_password == "":
                            print("enter something !!")
                        elif get_password == "Y" :
                            break 
                        elif get_password == "N":
                            break
                    pwd_attempt = 2
                    while get_password == "Y" :                   
                        pwd = input("verify your password :")
                        if user_data.verify_password(pwd) :
                            user_data.get_password_when_requested(get_service_name)
                            break
                        elif pwd_attempt > 0 :
                            print(f"incorrect password 📛 you have {pwd_attempt} left ")
                            pwd_attempt -=1 
                        else :
                            print("an error occurred 📛 ")
                            me.log_out()                        
                            break
                else :
                    print("you don't have any credential !!")                  
            else :
                print("you need to log in first 📛")

        elif choice == "7":
            if me.current_user :
                len_credential = len(user_data.list_of_services())
                if len_credential != 0 :
                    while True :                       
                        number = input(f"enter the number of of that credential:")
                        if number.isdigit():
                            number = int(number)
                            if 1 <= number <= len_credential : 
                                get_service_name = user_data.list_of_services()[number-1]
                                user_data.delete_credential(get_service_name)
                                print(f"you successfully deleted :{get_service_name} ✅")
                                break
                            else :
                                print("not okay !")
                        else :
                            print("enter a nummber !!")
                else :
                    print("you don't have any credential !! ")
            else :
                print("you need to log in first !")

        elif choice == "8":
            is_running = False
        else :
            print("📛invalid input 📛")


if __name__ == '__main__':
    main()



