import random, string
from random import randrange

# generate ai answer
num = randrange(1,3)
ans = ''
if num == 1:
    ans = "rock"
elif num == 2:
    ans = "scissors"
elif num == 3:
    ans = "paper"

# players answer
input = input("Rock Paper Scissors? \n \n").lower()
if input == "rock":
    print(f"ai says {ans}!")
    if ans == "rock":
        print("Tie!")
    elif ans == "paper":
        print("You lose!")
    elif ans == "scissors":
        print("You win! :)")

elif input == "scissors":
    print(f"ai says {ans}!")
    if ans == "rock":
        print("You lose!")
    elif ans == "paper":
        print("You win! :)")
    elif ans == "scissors":
        print("Tie!")
    
elif input == "paper":
    print(f"ai says {ans}!")
    if ans == "rock":
        print("You win! :)")
    elif ans == "paper":
        print("Tie!")
    elif ans == "scissors":
        print("You lose!")

else:
    print("Invalid, please try again.")    