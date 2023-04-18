import math

# Dante LoPriore
# January 20, 2022
# PS1: Problem 1

# Int Int Int -> Int 
# Purpose: allows the user to input three sides of a triangle a, b, c, 
# and prints the area of the triangle using Heron's formula.

# to represent side A of triangle based on user's input
a = int(input("Enter a number for side A of the triangle: "))

# to represent side B of triangle based on user's input
b = int(input("Enter a number for side B of the triangle: "))

# to represent side C of triangle based on user's input
c = int(input("Enter a number for side C of the triangle: "))

# variable to show a one half
half = 1/2

# to compute the s value
# aquire s by geting the sum of all sides and dividing it by 2
s = half*(a+b+c)

# to compute the area of the triangle using Heron's formula.
area = math.sqrt((s*(s-a)*(s-b)*(s-c)))

# output the final result which is the area of the triangle
print(area)




