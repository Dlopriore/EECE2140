# Dante LoPriore
# January 20, 2022
# PS1: Problem 4

# This verion of this problem was the more effficient way to complete this task
# I started from doing a 2D array to now a 1D array where I use multiplication of 
# strings to output the space and stars
# Got the motivation to do this by the lecture problem involving a triangle of numbers


# Purpose: to acquire a positive integer from the user and output an
# triangle of stars that looks like a tree which its height is the positive integer 
# the user choose

# allows user to input a positive integer which corilates to how many 
# rows the user wants in their triangle
n = int(input("Enter a positive integer n: "))


n = n + 1 #increment n since string slicng needs an extra value to alter the full string

# to represent the equilaterial triangle of stars with the size based on the 
# positive integer n
space = " "
stars = "*"
for i in range(1, n):
    # to output how many spaces are needed in that row
    print(space*(n-i), end="")

    # to output how many stars are needed in that row
    print(stars*((2*i)-1))




