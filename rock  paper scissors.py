#simple Rock,Paper,Scissors game :
import random
game = ["rock","paper","scissor"]
is_running = True
while  is_running:
    computer = random.choice(game)
    name = None
    while name not in game :
        name = input("select form (rock ,scissor, paper) :").lower()
    print(f"you choose {name}")
    print(f"the computer choose :{computer}")
    if computer == name:
        print("that's a draw")
    elif name =="paper" and computer == "rock":
        print("you win")
    elif name == "rock" and computer == "scissor":
        print("you win")
    elif name == "scissor" and computer== "paper"   :
        print("you win")
    else :
        print("you lose")
    play_again = input("do you want to play again (y/n)??").lower()
    if not play_again == "y":
        is_running = False








# advance Rock,Paper,Scissors
import random 
choices = ["rock","paper","scissor"]

def game():
    print("------------------------------------------------------------------------")
    print("the rules :")
    print("you will play with the computer 5 matches to determine who is the winner ")
    print("------------------------------------------------------------------------")
    rounds = 5 
    win_result = 0
    lose_result = 0
    draw_result = 0
    while rounds >0 :
        if win_result == 3 or lose_result == 3 :
            break
        user_turn = input("enter your choice :").lower().strip()
        if user_turn not in choices :
            print("invalid input enter (rock/paper/scissor) !📛")
            continue
        computer = random.choice(choices)
        print("***************************")
        print(f"your choice :{user_turn}")
        print(f"the computer's choice :{computer}")
        print("***************************")
        if user_turn == computer :
            print("this is a draw 🤝")
            draw_result +=1
        elif (user_turn == "rock" and computer == "paper") or \
              (user_turn == "paper" and computer == "scissor") \
                or (user_turn == "scissor" and computer == "rock"):
            print("you lose 👎☹️")
            lose_result +=1      
        else :
            print("you won 🎉😁")
            win_result += 1
        rounds -= 1      
    print("\n---- the result of this round ----")
    print(f"you won :{win_result} times")
    print(f"you lose :{lose_result} times")
    print(f"you draw with the computer : {draw_result} times")
    print("-----------------------------------")
    if win_result > lose_result :
        print(f"congratulations ,you won this round !")
    elif win_result < lose_result :
        print("unfortunately you lose this round ,good luck next time")
    else :
        print("its a draw !!")
    print("-----------------------------------\n")
        

def main() :
    is_running = True 
    while is_running :
        print("-----------------------------------------")
        print("wecome to the game of rock,paper,scissor ")
        print("-----------------------------------------")
        user_choice = input("do you want to play a game ?(yes/no):").lower()
        if user_choice == "yes" :
            game()
        elif user_choice == "no":
            is_running = False 
        else :
            print("⛔invalid input⛔")

if __name__=='__main__':
    main()
