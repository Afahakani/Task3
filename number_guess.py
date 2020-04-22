# A number guessing game with three levels: Easy, Medium and Hard
# For Easy, secret number is 5
# For Medium, secret number is 15
# For Hard, secret number is 45


# defining the easy level and calling the execution program
def easy_game():
    print("Easy Level")
    print("In this level, you are expected to guess any number between 1 and 10 and you have 6 guesses to make")
    execution(5, 0, 6, 10)


# defining the medium level and calling the execution program
def medium_game():
    print("Medium Level")
    print("In this level, you are expected to guess any number between 1 and 20 and you have 4 guesses to make")
    execution(15, 0, 4, 20)


# defining the hard level and calling the execution program
def hard_game():
    print("Hard Level")
    print("In this level, you are expected to guess any number between 1 and 50 and you have only 3 guesses to make")
    execution(45, 0, 3, 50)


# the execution program for the game
def execution(secret_number, guess_count, guess_limit, last_digit):
    num_range = list(range(1, last_digit+1))
    while guess_count < guess_limit:
        try:
            guess = int(input("Enter your guess number: "))
            if guess not in num_range:
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
            print("You are expected to enter only numbers")
    else:
        print("Game Over!")
    exit(0)


# creating the game's different levels and calling the user's choice
def guessing_game():
    print("""Welcome to Number Guessing Game!
There are three Levels in this game: Choose any to play
    Easy
    Medium
    Hard """)
    user_choice = input("Enter your game level choice: ").lower()
    if user_choice == "easy":
        easy_game()
    elif user_choice == "medium":
        medium_game()
    elif user_choice == "hard":
        hard_game()
    else:
        print("Sorry! You entered a wrong choice")
        exit(0)


# calling the game function to execute the program
guessing_game()
