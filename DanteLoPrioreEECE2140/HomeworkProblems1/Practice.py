import random

secret_number = random.randint(1,100)
turns = 10
while turns > 0:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess == secret_number:
      print("You guessed it right!")
      break
    elif guess > secret_number:
      print("Too high. You have {} turns left.".format(turns-1))
    else:
      print("Too low. You have {} turns left.".format(turns-1))
    turns -= 1
if turns == 0:
    print("You ran out of turns. The secret number was {}.".format(secret_number))
play_again = input("Do you want to play again? (yes/no) ")
if play_again.lower() == "yes":
    secret_number = random.randint(1,100)
    turns = 10
    while turns > 0:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess == secret_number:
          print("You guessed it right!")
          break
        elif guess > secret_number:
          print("Too high. You have {} turns left.".format(turns-1))
        else:
          print("Too low. You have {} turns left.".format(turns-1))
        turns -= 1
    if turns == 0:
        print("You ran out of turns. The secret number was {}.".format(secret_number))
    play_again = input("Do you want to play again? (yes/no) ")

