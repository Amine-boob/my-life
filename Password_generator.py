# all project rely on password ganerator :

# password generator (my effort)
import random
import string
print("*************************************")
print("Welcome to this password generator ")
print("*************************************")

password_length = int(input("how length you want your password to be :"))

def name() :
    namee = input("do you want to add your name to this password (y/n)?").lower()
    if namee == "y" :
        name_input = input("enter your name :")
        return name_input
    else :
        return None

some_list = []
character = string.digits +string.ascii_letters + string.punctuation

user_name = name()

if user_name :
    number = len(user_name)
    some_list.append(user_name)
else :
    number = 0

for i in range(password_length - number) :
    symbol_part = "".join(random.choice(character))
    some_list.append(symbol_part)

for x in  some_list :
    print("you password is :")
    print(x,end="")



#chat gpt :
import random
import string
print("*************************************")
print("Welcome to this password generator ")
print("*************************************")

password_length = int(input("how length you want your password to be :"))

def get_name() :
    namee = input("do you want to add your name to this password (y/n)?").lower()
    if namee == "y" :
        name_input = input("enter your name :")
        return name_input
    else :
        return ""

character = string.digits + string.ascii_letters + string.punctuation
password = get_name()

for x in range(password_length - len(password)):
    password += random.choice(character)

print(f"your password is :{password}")





# generate password but it append each password to a file
import random
import string

is_running = True
while is_running :
    file_path = "myfile"
    print("\n*************************************")
    print("Welcome to this password generator ")
    print("*************************************\n")
    password_length = int(input("how length you want your password to be :"))
    def get_name() :
        namee = input("do you want to add your name to this password (y/n)?").lower()
        if namee == "y" :
            name_input = input("enter your name :")
            return name_input
        else :
            return ""
    character = string.digits + string.ascii_letters + string.punctuation
    password = get_name()
    for x in range(password_length - len(password)):
        password += random.choice(character)
    print(f"your password is :{password}")
    with open(file_path,"a") as file :
        file.write(password + "\n" + "-"*20 + "\n")

        print("saved in :",file_path)

    try_again = input("do you want to try again (y/n):").lower()
    if try_again == "n":
        is_running = False




# password generator in GUI 
import sys
import random
import string
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QApplication, QVBoxLayout, QHBoxLayout, QMenuBar, \
	QAction,QTextEdit
from PyQt5.QtCore import Qt

class PasswordGenerator(QWidget) :
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Password Generator")
		self.setWindowIcon(QIcon("tokyo-ghoul.jpg"))  
		self.resize(400,400)
		self.move(800,0)
		self.greeting_label = QLabel("Welcome to password\ngenerator\n------------------------",self)
		self.question_label = QLabel("How length of your password ?",self)
		self.input = QLineEdit(self)
		self.button_yes = QPushButton("Yes/Okay",self)
		self.button_no = QPushButton("no",self)
		self.describe_label = QLabel("saved !",self)
		self.characters = string.ascii_letters + string.digits+string.punctuation
		self.add_passwords = []
		self.password_length = 0
		self.password = ""
		self.file_name = ""
		self.desktop_path = "C:\\Users\\hhh\\Desktop\\"

		self.windows = []
		self.initUI()
		self.create_menu()

	def create_menu(self):
		main_menu = QMenuBar(self)
		file_menu = main_menu.addMenu("file")
		edit_menu = main_menu.addMenu("edit")

		add_window = QAction("See result",self)
		add_window.triggered.connect(self.add_window)
		file_menu.addAction(add_window)

		quit_option = QAction("Quit", self)
		quit_option.triggered.connect(self.close)
		quit_option.setShortcut(QKeySequence("ctrl+Q"))
		file_menu.addAction(quit_option)

	def initUI(self):
		vbox = QVBoxLayout()
		vbox.addSpacing(30)
		vbox.addWidget(self.greeting_label)
		vbox.addWidget(self.question_label)
		vbox.addWidget(self.input)
		vbox.addSpacing(20)
		hbox = QHBoxLayout()
		hbox.addWidget(self.button_yes)
		hbox.addWidget(self.button_no)
		vbox.addLayout(hbox)
		vbox.addWidget(self.describe_label)
		self.setLayout(vbox)

		self.greeting_label.setObjectName("greeting_label")
		self.question_label.setObjectName("question_label")
		self.input.setObjectName("input")
		self.describe_label.setObjectName("describe_label")
		self.setStyleSheet("""
			QPushButton{
				font-size:30px;
			}
			QLabel#greeting_label{
				font-size:35px;
			}
			QLabel#question_label{
				font-size:30px;
			}
			QLineEdit#input{
				font-size:30px;
			}
			QLabel#describe_label{
				font-size:30px;
			}		
		""")
		self.greeting_label.setAlignment(Qt.AlignCenter)
		self.describe_label.setAlignment(Qt.AlignCenter)

		self.button_yes.clicked.connect(self.click_yes)
		self.button_no.clicked.connect(self.click_no)

	def click_yes(self):
		click = self.button_yes.clicked
		text = self.input.text()
		question = self.question_label.text()
		if  click and question == "How length of your password ?":
			self.password_length += int(text)
			self.question_label.setText("Do you want to add your name in\nthe password (press Y/N)?")
			self.input.setText("")
		elif click and question == "Do you want to add your name in\nthe password (press Y/N)?" :
			self.question_label.setText("Add your name below")
			self.input.setPlaceholderText("Enter your name")
			self.input.setText("")
		elif click and question == "Add your name below" :
			self.password += text
			self.input.setText("")
			self.input.setPlaceholderText("")
			self.question_label.setText("Do you want to save this\npassword in a file(press Y/N)?")
		elif click and question == "Do you want to save this\npassword in a file(press Y/N)?" :
			self.question_label.setText("Write the file name below ")
			self.input.setPlaceholderText("Write the file name")
			self.generate_password()
			# to add the password to the list of passwords 
			self.add_passwords.append(self.password)
		elif click and question == "Write the file name below ":
			self.question_label.setText("Do you want to try again ?")
			self.file_name += text
			self.input.setText("")
			self.describe_label.setText(f"your password is :'{self.password}'\nsaved in '{self.file_name}'")
			self.add_data_to_file()
		elif click and question == "Do you want to try again ?":
			self.question_label.setText("How length of your password ?")
			self.describe_label.setText("")
			self.input.setPlaceholderText("")
			self.password_length = 0
			self.password = ""
			self.file_name = ""

	def click_no(self):
		click = self.button_yes.clicked
		text = self.input.text()
		question = self.question_label.text()
		if click and question =="Do you want to add your name in\nthe password (press Y/N)?" :
			self.question_label.setText("Do you want to save this\npassword in a file(press Y/N)?")

		elif click and question == "Do you want to save this\npassword in a file(press Y/N)?" :
			self.question_label.setText("Do you want to try again ?")
			self.generate_password()
			self.add_passwords.append(self.password)
			self.describe_label.setText(f"your password is '{self.password }'")
		elif click and question == "Do you want to try again ?" :
			self.describe_label.setText("have a nice day\nyou can check all your passwords")
		else :
			self.describe_label.setText("📛invalid button📛")

	def add_data_to_file(self):
		with open(self.file_name ,"a") as file :
			file.write(self.password + "\n" + "-"*20 +"\n")
		with open(self.desktop_path+self.file_name ,"a") as file :
			file.write(self.password + "\n" + "-" * 20 + "\n")

	def generate_password(self):
		for x in range(self.password_length - len(self.password)) :
			self.password += random.choice(self.characters)
	# a function to call the data to add it to TextEdit
	def add_data_to_text(self,text_widget):
		# every time to open the new window the system will delete what inside
		text_widget.clear()
		# then add a new data from the list
		for x in self.add_passwords :
			text_widget.append(x)

	def add_window(self):
		new_window = QWidget()
		new_window.setWindowTitle(f"Window #{len(self.windows) +1}")
		new_window.resize(300,400)
		new_window.move(100,100)
		# add MenuBar to the new window
		main_bar = QMenuBar(new_window)
		file_bar = main_bar.addMenu("file")
		edit_bar = main_bar.addMenu("edit")
		# refresh option
		refresh_option =QAction("Refresh", new_window)
			# you need here to connect it to a function that update display :
		refresh_option.triggered.connect(lambda : self.add_data_to_text(new_window.text))
		refresh_option.setShortcut(QKeySequence("Ctrl+R"))
		file_bar.addAction(refresh_option)
		# quit option
		quit_option = QAction("Quit",new_window)
		quit_option.setShortcut(QKeySequence("Ctrl+Q"))
		quit_option.triggered.connect(new_window.close)
		file_bar.addAction(quit_option)
		#add label
		new_window.label = QLabel("All passwords :",new_window)
		# add TextEdit
		new_window.text = QTextEdit(new_window)
		# align everything
		vbox = QVBoxLayout()
		vbox.addSpacing(30)
		vbox.addWidget(new_window.label)
		vbox.addSpacing(20)
		vbox.addWidget(new_window.text)
		new_window.setLayout(vbox)
		# edit size of font
		new_window.label.setStyleSheet("font-size:30px;")
		new_window.text.setStyleSheet("font-size:20px;")
		self.add_data_to_text(new_window.text)

		new_window.show()
		self.windows.append(new_window)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = PasswordGenerator()
	window.show()
	sys.exit(app.exec_())
