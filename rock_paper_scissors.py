import random

user_win=0
computer_win=0
draw=0


option=["rock","paper","scissor"]
while True:
    user_input=input("type rock/paper/scissor or Q to Quit: ").lower()
    if user_input=="q":
       break

    if user_input not in option:
        continue


    random_number= random.randint(0,2)
    
    computer_pick= option[random_number]
    print("computer picked",computer_pick + ".")

    if user_input=="rock" and computer_pick== "scissor":
        print("you won")
        user_win += 1
        

    elif user_input=="paper" and computer_pick== "rock":
        print("you won")
        user_win += 1
        

    elif user_input=="scissor" and computer_pick== "paper":
        print("you won")
        user_win += 1

    elif user_input==computer_pick:
        print("Draw")
        draw += 1

    else:
        print("You lost")
        computer_win +=1
   

print("You won", user_win, "times" )
print("computer won", computer_win, "times")
print("draw", draw, "times")
print("Goodbye!")