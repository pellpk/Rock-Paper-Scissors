import random, string
from random import randrange

# recursive function that can loop under certain conditions
def gameLoop():
    # gets users choice and checks it is valid
    userAnswer = input("Rock Paper Scissors? \n \n").lower()
    if userAnswer != "rock" and userAnswer != "paper" and userAnswer != "scissors":
        print("Invalid choice!\n")
        gameLoop()# if invalid, repeats question
        return
    
    # generate computer answer
    randomNum = randrange(1,3)
    if randomNum == 1:
        compAnswer = "rock"
    elif randomNum == 2:
        compAnswer = "scissors"
    elif randomNum == 3:
        compAnswer = "paper"
    print(f"ai says {compAnswer}!")

    # logic to decide winner, repeats gameLoop if results in a tie
    if userAnswer == "rock":
        if compAnswer == "rock":
            print("Tie! lets go againd!\n")
            gameLoop()
            return
        elif compAnswer == "paper":
            print("You lose!")
        elif compAnswer == "scissors":
            print("You win! :")

    elif userAnswer == "scissors":
        if compAnswer == "rock":
            print("You lose!")
        elif compAnswer == "paper":
            print("You win! :")
        elif compAnswer == "scissors":
            print("Tie! lets go againd!\n")
            gameLoop()
            return
        
    elif userAnswer == "paper":
        if compAnswer == "rock":
            print("You win!")
        elif compAnswer == "paper":
            print("Tie! lets go againd!\n")
            gameLoop()
        elif compAnswer == "scissors":
            print("You lose!")

# starts the game
gameLoop()