#"this program called (note manager) with the possibility to register ,
# log in and log out  with features of :  add note ,show notes ,delete a note 
#plus all the data will saved in a file called (database.pkl)in your desktop every time you 
#enter to the application you will find your data still there "
import hashlib
import pickle
import os

class User : 
    def __init__(self,username,password) :
        self.username = username 
        self.password = password 
        self.notes = []

    def verify_password(self,password):
        if password == self.password :
            return True 
        else :
            return False  

class NoteManager :
    def __init__(self) :
        self.path = os.path.expanduser("~/Desktop")
        self.path_to_database = os.path.join(self.path,"database.plk")
        self.all_users = []
        self.current_user = ""
    
    # ---------- File Handling ----------
    def get_data_from_file(self):      #if the file exist fetch data from it and put it in self.all users:
        try :
            with open(self.path_to_database ,"rb") as file :
                data = pickle.load(file)
                self.all_users = data
        except FileNotFoundError :
            with open(self.path_to_database ,"wb") as file :
                pickle.dump(self.all_users,file)
    def submit_data_to_file(self,user,pwd):
        with open(self.path_to_database , "rb") as file :
            data = pickle.load(file)
            data.append(User(user,pwd))    
        with open(self.path_to_database,"wb") as file :
            pickle.dump(data,file) 
    def save_data(self) : # the role of this function is to save any changes that happens to the file automatic
        with open(self.path_to_database ,"wb") as file :
            pickle.dump(self.all_users,file)

    # ---------- Authentication ----------
    def register(self):
        #is_running = True 
        while True :
            name = input("enter your name (q to quit):")
            if name == "":
                print("enter something 📛")
            elif name == "q" :
                return 
            elif name in self.all_user_names() :
                print("this name already exist 📛")
            else :
                print("valid username ✅")
                break        
        while True :
            password = input("set a password (q to quit):")
            if password == "":
                print("enter something 📛")
            elif password == "q":
                return
            else :               
                self.current_user = name
                hash_pwd = self.hash_password(password)
                self.submit_data_to_file(name,hash_pwd)           
                self.all_users.append(User(name,hash_pwd))
                self.save_data()
                print("account created ✅")
                break
    def log_in(self):
        while True :
            name = input("verify your name (q to quit):")
            if name == "":
                print("enter something 📛")
            elif name == "q" :
                return 
            elif name in self.all_user_names() :
                print("username found ✅")
                break 
            else :
                print("username not found")
        password_attempt = 2
        while True :
            password = input("verify your password (q to quit)")
            if password == "":
                print("enter something 📛")
            elif password == "q" :
                return          
            hash_password = self.hash_password(password)
            if self.get_user_data(name).verify_password(hash_password) :
                print("password correct ✅")
                print("you succsessfully logged in ")
                self.current_user = name
                break 
            elif password_attempt > 0 :
                print(f"you have {password_attempt} left 📛")
                password_attempt -= 1 
            else :
                print("failed to log in try again later 📛")
                return                   
    def log_out(self):
        if self.current_user :
            self.current_user = ""
            print("you successfully logged out ✅")
        else :
            print("you are already logged out 📛")

    # ---------- Notes Management ----------
    def add_note(self,note):     
        self.get_user_data(self.current_user).notes.append(note)
        print("note successfully added ✅")
        self.save_data()
    def show_notes(self):
        user_data = self.get_user_data(self.current_user)
        user_notes = user_data.notes
        if not user_notes :
            print("you don't have any notes 📛")
            return
        print("\n------- your notes -------")
        for index,value in enumerate(user_notes ,start=1) :
            print(f"{index} - {value}")
        print("--------------------------\n")
    def delete_note(self,index) :
        user_data = self.get_user_data(self.current_user)
        get_note_to_delete = user_data.notes[index-1]
        user_data.notes.remove(get_note_to_delete)
        self.save_data()
        print("note successfully deleted ✅")


    def hash_password(self,password) :
        return hashlib.sha256(password.encode()).hexdigest()

    def all_user_names(self):
        names = []
        for user in self.all_users :
            names.append(user.username)
        return names

    def get_user_data(self,current) :
        for user in self.all_users :
            if user.username == current :
                return user 
        return None 
    
def main():
    is_running = True 
    me = NoteManager()
    me.get_data_from_file()
    while is_running :
        if me.current_user :
            user_data = me.get_user_data(me.current_user)
        print("------ note manager ------")
        print(f"Hello {me.current_user}")
        print("--------------------------")
        print("1 - register ")
        print("2 - log in ")
        print("3 - log out ")
        print("4 - show my notes")
        print("5 - add a note ")
        print("6 - delete a note ")
        print("7 - quit")
        print("---------------------------")
        choice = input("enter your choice :")
        if choice == "1" :
            me.register()
        elif choice == "2" :
            me.log_in()
        elif choice == "3" :
            me.log_out()
        elif choice == "4" :
            if me.current_user :
                me.show_notes()   
            else :
                 print("you need to log in first 📛")
        elif choice == "5" :
            if me.current_user :
                while True :
                    note = input("enter your note :")
                    if note == "":
                        print("enter something 📛")
                    else :
                        me.add_note(note)
                        break
            else :
                print("you need to log in first 📛")
        elif choice == "6" :
            if me.current_user :
                if len(user_data.notes ) != 0 :
                    while True :
                        number = input("enter the number of the note :")
                        if number.isdigit():
                            number = int(number)
                            if 1 <= number <= len(user_data.notes) :
                                me.delete_note(number)
                                break
                            else :
                                print("your number out of the range 📛")
                        else :
                            print("enter a number 📛")
                else :
                    print("you don't have any notes 📛")
            else :
                print("you need to log in first 📛")
        elif choice == "7" :
            is_running = False 
        else :
            print("invalid input")
    
if __name__ == '__main__':
    main()
