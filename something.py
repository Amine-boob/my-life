print("hello world")

print("hello world")

# program to change from m to cm
change = float(input("enter your number :"))
unit =input("enter the unit (cm,m) :")
if unit == "cm":
    number = change / 1000
    print(f"your new number is {number}m")
elif unit == "m":
    number = change * 1000
    print(f"your new number is {number}cm")
elif change == "":
    print("please enter something ")


food = input("enter all your favorits foods (no , sorts of food ) :")
while not food == "no":
    print("that so delicious ")
    food = input("enter another sort of food :")
print("good by")



num = int(input("enter a number from 1 to 10 :"))
while num<1 or num>10 :
    print("You have not completed the requirements ")
    num = int(input("enter another number from 1 to 10 :"))
print("now put this number in your ass ~_~")

for x in range(1,11):
    print(x)


for x in range(1,22):
    if x == 19:
        break
    print(x)


#this example is long and hard to explain
import time

time1 = 61
for x in reversed(range(0 , time1)):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)
#this fuction above is necessery to tell to the system to wait one second then move to the next number ,
#
print("wake up now !!!")
