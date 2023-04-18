import random
# Dante LoPriore
# January 31, 2023
# PS2: Problem 4

# Purpose: to game based on the classic race of the tortoise and the hare
# using a random number generation to create a simulation of the race.

# initialiaze the variables for the position of the hare and tortoise
# Both players begin the race at square 1 of 95.
tortoise_position = 1
hare_position = 1
tortoise_win_count = 0
hare_win_count = 0
tie_count = 0
game_number = 0
FINISH_LINE = 95

# -> Str
# to compute the tortoise's overall movement using a random number generator based on the probability given in the problem.
def tortoise_prob():
   # to create and assign a random number
   random_number_generated = random.randint(1,20)

   # to determine what the tortoise's next movement would be based on
   # if the generated random number fits within a a certain range or a probability
   if ((1 <= random_number_generated) and (random_number_generated <= 8)):
       return ("Fast Plod")
   if ((9 <= random_number_generated) and (random_number_generated <= 10)):
       return ("Slip")
   if ((11 <= random_number_generated) and (random_number_generated <= 20)):
       return ("Slow Plod")


# -> Str
# to compute the hare's overall movement using a random number generator based on the probability given in the problem.
def hare_prob():
   # to create and assign a random number
   random_number_generated = random.randint(1,20)


   # to determine what the hare's next movement would be based on
   # if the generated random number fits within a a certain range or a probability
   if ((1 <= random_number_generated) and (random_number_generated <= 2)):
       return ("Sleep")
   if ((3 <= random_number_generated) and (random_number_generated <= 8)):
       return ("Big Hop")
   if ((9 <= random_number_generated) and (random_number_generated <= 10)):
       return ("Big Slip")
   if ((11 <= random_number_generated) and (random_number_generated <= 14)):
       return ("Small Hop")
   if ((15 <= random_number_generated) and (random_number_generated <= 20)):
       return ("Small Slip")


# to display the starting positions for the hare and tortoise
print("BANG! AND THEY'RE OFF!!!!!")
print(" T", "-"*(FINISH_LINE-1))
print(" H", "-"*(FINISH_LINE-1))


# to run the game 50 times to understand the win ratio between the two contenders
while game_number < 50:

   # activates the gameplay for a game
   # the game will end when a contender goes beyond the finish line
   while((hare_position < FINISH_LINE) and (tortoise_position < FINISH_LINE)):

       # to determine the tortoise's next move base on its probability
       if(tortoise_prob() == "Fast Plod"):
           tortoise_position = tortoise_position +3
       if(tortoise_prob() == "Slip"):
           tortoise_position = tortoise_position -6
       if(tortoise_prob() in "Slow Plod"):
           tortoise_position = tortoise_position +1
      
       # to determine the hare's next move base on its probability
       if(hare_prob() in "Sleep"):
           hare_position = hare_position
       if(hare_prob() in "Big Hop"):
           hare_position = hare_position + 9
       if(hare_prob() in "Big Slip"):
           hare_position = hare_position -12
       if(hare_prob() in "Small Hop"):
           hare_position = hare_position +1
       if(hare_prob() in "Small Slip"):
           hare_position = hare_position -2
      
       # to display the tortoise's movement and position during the game
       if(tortoise_position <= 0):
           # resets the tortoise's position to square 1
           # if its negative motion goes beyond square 1
           tortoise_position = 1
           print(" T", "-"*(FINISH_LINE - 1))
       else:
           print("-"*(tortoise_position-1), "T", "-"*(FINISH_LINE - tortoise_position))
      
       # to display the hare's movement and position during the game
       if(hare_position <= 0):
           # resets the hare's position to square 1
           # if its negative motion goes beyond square 1
           hare_position = 1
           print(" H", "-"*(FINISH_LINE - 1))
       else:
           print("-"*(hare_position-1), "H", "-"*(FINISH_LINE - hare_position))

       # to determine whether the tortoise and hare are in the same position
       if(tortoise_position == hare_position):
           print("OUCH!!!")
  
   #to determine whether the two contenders tied the game
   if((tortoise_position == hare_position) and (tortoise_position >= FINISH_LINE) and (hare_position >= FINISH_LINE)):
       print("OUCH!!!")
       print("Tie")
       print("-")
       game_number = game_number + 1 #increments the game count by one
       tie_count = tie_count + 1 #increments the tie count by one
       # to display the starting positions for the hare and tortoise
       # reset game mechanics
       tortoise_position = 1
       hare_position = 1
       if(game_number < 50):
           print(" T", "-"*(FINISH_LINE-1))
           print(" H", "-"*(FINISH_LINE-1))
  
   #to determine whether the Tortoise won the game
   if((tortoise_position >= FINISH_LINE) and ((hare_position < FINISH_LINE))):
       print("TORTOISE WINS!!! YAY!!!")
       tortoise_win_count = tortoise_win_count + 1 #increments the win count by one
       game_number = game_number + 1 #increments the game count by one


       # to display the starting positions for the hare and tortoise
       # reset game mechanics
       tortoise_position = 1
       hare_position = 1
       if(game_number < 50):
           print("BANG! AND THEY'RE OFF!!!!!")
           print(" T", "-"*(FINISH_LINE-1))
           print(" H", "-"*(FINISH_LINE-1))
      
   #to determine whether the Hare won the game
   if((tortoise_position < FINISH_LINE) and ((hare_position >= FINISH_LINE))):
       print("HARE WINS. YUCH!")
       hare_win_count = hare_win_count + 1  #increments the win count by one
       game_number = game_number + 1  #increments the game count by one

       # to display the starting positions for the hare and tortoise
       # reset game mechanics
       tortoise_position = 1
       hare_position = 1
       if(game_number < 50):
           print("BANG! AND THEY'RE OFF!!!!!")
           print(" T", "-"*(FINISH_LINE-1))
           print(" H", "-"*(FINISH_LINE-1))


# outputs the win and tie ratio for the two contenders playing the games
print('\n')
print(f'The Hare had won {hare_win_count} games')
print(f'The Tortoise had won {tortoise_win_count} games')
print(f'The two contenders had tied {tie_count} games')
