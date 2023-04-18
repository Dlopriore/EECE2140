import math

# Dante LoPriore
# January 20, 2022
# PS1: Problem 3

# Int Int -> Int 
# Purpose: to aquire two numbers from the user and an operator 
# then display the result of the operation

# to represent the user's inputs for the first and second number
firstNumber = int(input("Enter your first number: "))
secondNumber = int(input("Enter your second number: "))

# to represent the user's inputs for the desired operation to be used on the numbers
operator = input("Enter an operation: ")

# to determine what operation to preform
# then it will preform the operation and output the final result
if(operator == '+'):
    print(f'{firstNumber} + {secondNumber} = {firstNumber+secondNumber}')
if(operator == '-'):
    print(f'{firstNumber} - {secondNumber} = {firstNumber-secondNumber}')
if(operator == '*'):
    print(f'{firstNumber} * {secondNumber} = {firstNumber*secondNumber}')
if(operator == '/'):
    print(f'{firstNumber} / {secondNumber} = {firstNumber/secondNumber}')
