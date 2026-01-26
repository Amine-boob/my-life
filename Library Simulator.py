# Library Management Simulator
class User :
    def __init__(self,username):
        self.username = username
        self.my_books = []
    def borrow(self,name):
        self.my_books.append(name)

class Book :
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True
    def toggle(self):
        self.is_available = not self.is_available

class Library :
    def __init__(self):
        # books that already in the library
        self.all_books = [Book("1984","George Orwell"),
                          Book("Harry Potter","J.K.Rowling"),
                          Book("Deep Work","Cal Newport"),
                          Book("Dracula","Bram Stoker"),
                          Book("The Art of Invisibility","Kevin Mitnick")]
        self.all_users = []
        self.the_user = ""

    def borrow_a_book(self):
        if self.the_user :
            num = self.get_book_number(self.all_books)
            new_index = num - 1
            if self.all_books[new_index].is_available :
                for user in self.all_users :
                    if user.username == self.the_user :
                        user.borrow(self.all_books[new_index])
                        self.all_books[new_index].toggle()
                        print(f"you successfully borrowed '{self.all_books[new_index].title}' ✅")
            else :
                print("this book is not available right now 📛")
        else :
            print("you need to show your ID first 📛")

    def get_username(self):
        is_run = True
        while is_run :
            all_names = []
            name = input("enter your name (q to quit):")
            if name == "":
                print("enter something ")
            elif name == "q"or name == "Q" :
                print("try again later ")
                break
            else :
                for user in self.all_users:
                    all_names.append(user.username)
                if name in all_names :
                    self.the_user = name
                    is_run = False
                else :
                    self.the_user = name
                    self.all_users.append(User(name))
                    is_run = False

    def get_book_number(self,second_number):
        while True :
            try :
                num = int(input("enter the book number :"))
                if 1 <= num <= len(second_number) :
                    return num
                else :
                    print("enter book's number 📛")
            except ValueError :
                print("enter just digits !📛")

    def add_book(self):
        is_run = True
        while is_run :
            book_title = input("enter the title of that book :")
            if book_title =="":
                print("enter something !📛")
            else :
                while True :
                    book_author = input("enter the name of the author :")
                    if book_author == "":
                        print("enter something !📛")
                    else :
                        self.all_books.append(Book(book_title,book_author))
                        is_run = False
                        break

    def show_my_books(self):
        if self.the_user :
            for user in self.all_users :
                if user.username == self.the_user :
                    if user.my_books :
                        print("\n------ your books ------")
                        for index,book in enumerate(user.my_books ,start=1):
                            print(f"{index} - {book.title}")
                        print("-------------------------\n")
                    else :
                        print("you don't have any books yet 📛")
        else :
            print("you need to show your ID first 📛")

    def show_books(self):
        print("\n-------------------------------------")
        print("--- here all the books that exist ---")
        print("-------------------------------------")
        for index,book in enumerate(self.all_books , start=1) :
            state = "--> Available✅" if book.is_available else "--> Not available❌"
            print(f"{index} - {book.title:30} by   {book.author:20} {state}")
        print("-------------------------------------\n")

    def return_book(self):
        if self.the_user :
            for user in self.all_users :
                if user.username == self.the_user :
                    num = self.get_book_number(user.my_books)
                    new_index = num -1
                    deleted = user.my_books.pop(new_index)
                    for book in self.all_books :
                        if book.title == deleted.title :
                            book.toggle()
                    print(f"you successfully put the book back '{deleted.title}'")
        else :
            print("you need to show ID first 📛")

def main():
    is_running = True
    me = Library()
    while is_running :
        print("------ LIBRARY ------")
        print(f"hello {me.the_user}")
        print("---------------------")
        print("1 - add a book ")
        print("2 - show ID ")
        print("3 - show my books ")
        print("4 - show all books in the library ")
        print("5 - borrow a book")
        print("6 - return a book ")
        print("7 - quit")
        print("---------------------")
        choice = input("enter a number :")
        if choice=="1":
            me.add_book()
        elif choice== "2":
            me.get_username()
        elif choice == "3" :
            me.show_my_books()
        elif choice=="4":
            me.show_books()
        elif choice=="5":
            me.borrow_a_book()
        elif choice== "6":
            me.return_book()
        elif choice == "7" :
            print("goodbye , visit us later 👋🏼")
            is_running = False
        else :
            print("📛invalid input📛")

if __name__=='__main__':
    main()
