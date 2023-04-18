import random

# Dante LoPriore
# January 20, 2022
# PS1: Problem 4

# Purpose: construct a game to guess a number between 1-1000

# to represent an integer that was selected with a range between 1-1000
random_number = random.randint(1, 1000)

# allow user to enter a number between 1-1000
user_number_input = int(input("Enter a number between 1-1000: "))

# to represent the amount of attempts a single user can input in the game 
MAX_ATTEMPTS = 9
attempts = 0

# to respresent the reset button 
user_reset_button = "Y"


# to represenrt the the random number generator game 
# gameplay occurs based on user's input to either stop or continue the game
while(user_reset_button in "Y"):

    # to determine whether the game should resume or end by understanding whether 
    # the user was able to select the correct number or the game reach its max attempts
    while((user_number_input != random_number) and (((MAX_ATTEMPTS - attempts) > 0))):

        attempts = attempts + 1 #increment the attempts by 1

        # to determine if the number the user selected was 
        # greater than the correct number
        if((user_number_input > random_number)):

            # outputs message to say the number was too high and retry their selection
            print("\nThe number you choose was Wrong \nIt was too high")
            print(f'You have {MAX_ATTEMPTS - attempts+1} attempts left \n')
            user_number_input = int(input("Enter a new number between 1-100: "))
        else:

            # outputs message to say the number was too low and retry their selection
            print("'\nThe number you choose was Wrong \nIt was too low")
            print(f'You have {MAX_ATTEMPTS - attempts+1} attempts left \n')
            user_number_input = int(input("Enter a new number between 1-100: "))
    # to determine whether the user won the game by check to see 
    # if they entered the correct number
    if(user_number_input == random_number):
        print("Congratulations you Won the game")

        # to give user the option to stop or reset game
        user_reset_button = input("Write Y to restart or N to stop:")
        if(user_reset_button.upper() == "N"):

            # ends game
            break
        else:
            # resets game mechanics
            attempts = 0
            user_number_input = 0
            random_number = 0
            random_number = random_number + random.randint(1, 1000)

            user_number_input = int(input("Enter a new number between 1-100: "))
    if(0 == (MAX_ATTEMPTS - attempts)):
        print("Game Over. You have reached your max attempts")
        print(f'The secret number was {random_number} \n')

        # to give user the option to stop or reset game
        user_reset_button = input("Write Y to restart or N to stop:")
        if(user_reset_button.upper() in "Y"):

            # resets game mechanics
            attempts = 0
            user_number_input = 0
            random_number = 0
            random_number = random_number + random.randint(1, 1000)

            user_number_input = int(input("Enter a new number between 1-100: "))
        else:

            # ends game
            break



