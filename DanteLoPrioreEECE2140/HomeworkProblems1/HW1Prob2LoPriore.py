# Dante LoPriore
# January 23, 2022
# PS1: Problem 2

# Int -> Str
# Purpose: to determine whether the user's integer input is deemed a palidrome 
# where the number of digits can be any number

# allow user to input a valid palindrome
user_number_input = int(input("Enter a Valid Palindrome: "))

# to initialize variables to store 
number_in_normal_order = user_number_input
number_in_reversed_order = 0

# to extract the digits of the user's input number using modulo and
# put the digits in reverse order. move to next digit by using floor division.
while user_number_input > 0:
    remainder = user_number_input % 10
    number_in_reversed_order = remainder + (number_in_reversed_order*10)
    user_number_input =  user_number_input // 10

# output the result of the normal and reverse order
print(f'Normal Order: {number_in_normal_order}')
print(f'Reversed Order: {number_in_reversed_order}')

# to determine whether the inputed number is a palindrome 
# by checking if the normal and reversed order are the same
if(number_in_normal_order == number_in_reversed_order):
    print("The number you entered was a Valid Palidrome")
else:
    print("The number you entered was not a Valid Palidrome")