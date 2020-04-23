# A number guessing game with three difficulty levels: Easy, Medium and Hard
# the secret number is generated from a random code
# guess count is initially set to 0

import random


# defining the easy level and calling the execution function
def easy_level():
    print("Easy Level")
    print("In this level, you are expected to guess any number between 1 and 10 and you have 6 guesses to make")
    execution(6, 10)


# defining the medium level and calling the execution function
def medium_level():
    print("Medium Level")
    print("In this level, you are expected to guess any number between 1 and 20 and you have 4 guesses to make")
    execution(4, 20)


# defining the hard level and calling the execution function
def hard_level():
    print("Hard Level")
    print("In this level, you are expected to guess any number between 1 and 50 and you have only 3 guesses to make")
    execution(3, 50)


# this is the execution function for the game
# this function takes two arguments:
# the limit specified for the guesses in each level and also
# the last digit in the range of guess numbers for each level
def execution(guess_limit, last_digit):
    guess_count = 0
    secret_number = random.randint(1, last_digit)
    guess_range = list(range(1, last_digit+1))
    while guess_count < guess_limit:
        try:
            guess = int(input("Enter your guess number: "))
            if guess not in guess_range:
                print(guess, "is not in Range! Enter a number between 1 and " + str(last_digit))
                continue
            if guess == secret_number:
                print("You got it Right!")
                break
            else:
                print("That was Wrong")
                guess_count += 1
                print("You have " + str(guess_limit - guess_count) + " chance(s) remaining")
        except ValueError:
            print("Wrong Input! You are expected to enter only numbers")
    else:
        print("Game Over!")
    exit(0)


# creating the game's different levels and calling the user's choice
def guessing_game():
    print("""Welcome to Number Guessing Game!
There are three difficulty Levels in this game. Choose any to play:
    Easy
    Medium
    Hard """)
    user_choice = input("Enter your game level choice: ").lower()
    if user_choice == "easy":
        easy_level()
    elif user_choice == "medium":
        medium_level()
    elif user_choice == "hard":
        hard_level()
    else:
        print("Sorry! You entered a wrong choice")
        exit(0)


# calling the game function to execute the program
guessing_game()
