# import required modules

import random

#define the rules
options =["rock","paper","scissor"]
#create the game loop
while True:
    #Game implementation goes here
    
# capture user input
    user_action = input("Enter a choice (rock, paper, scissors): ").lower()
    
# computer's random choice
    computer_action = random.choice(options)
    print (f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    
# determine the winner
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if (computer_action== "scissors"):
            print("Rock smash scissors! You Win!")
        else:
            print("paper covers rock! You lose!")
    elif user_action =="paper":
        if (computer_action=='rock'):
            print("paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_action=="scissors":
        if (computer_action=="paper"):
            print("Scissors cuts paper! You win!")
        else:
            print("paper covers rock! You lose!")
    else:
        print("Invalid Input, Please Enter... Rock, Paper, scissors.")
        
#Replay Option
# Additional conditions to be added here
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break