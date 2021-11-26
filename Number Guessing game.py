
import random

while True:
    randNumber = random.randint(1, 100)
    userGuess = None
    guesses = 0

    print("**** WELCOME TO NUMBER GUESSING GAME ****")
    name = input("Please Enter Your Name:  ")
    print(f"Guess what computer selected from 1 To 100")

    while (userGuess != randNumber):
        userGuess = int(input(f"{name} Enter Your Guess:  "))
        guesses += 1

        if userGuess == randNumber:
            print(f"Yeah!!! {name} you Guessed It right!!!")
        else:
            if userGuess > randNumber:
                print(f"{name} You Guessed it Wrong ! Please Guess Smaller Number ")
            else:
                print(f"{name} You Guessed it Wrong ! Please Guess Larger Number")

    print(f"{name} You Guessed the number in {guesses} guesess ")
    # with open("projects/Highscore.txt", 'r')as f:
    #     Highscore = int(f.read())

    # if(guesses < Highscore):
    #     print("You have Just broken the Highscore\n")
    #     with open("projects/Highscore.txt", 'w')as f:
    #         f.write(guesses)
    user_choice = input("Want to Play again?(Yes/Exit)\n")
    if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
        continue
    else:
        break
