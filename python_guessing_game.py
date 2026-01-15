#python number guessing game :
import random
lowest_num = 1
highest_num =100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print(f"select a number between {lowest_num} and {highest_num} :")
while is_running:
    guess = input("enter your guess :")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess >highest_num or guess<lowest_num :
            print("this number invalid")
            print(f"please select a number between {lowest_num} and {highest_num} :")
        elif guess > answer :
            print("your number is too high")
        elif guess < answer :
            print("your number is too low ")
        else :
            print(f"correct the answer was {answer}")
            print(f"its took {guesses}")
            is_running= False
    else :
        print("your guss is invalid")
        print(f"please select a number between {lowest_num} and {highest_num} :")
