# Dante LoPriore
# January 20, 2022
# PS1: Problem 5

# allows the user to enter a positive integer 
n = int(input("Enter the first n numbers in the Fibonacci Sequence: "))

# to represent the starting numbers of a fibonacci sequence
# first number is always zero
# first number is always one  
first_Position_Fibonacci = 0
second_Position_Fibonacci = 1

# to represent the sum of the next position 
sum_Next_Position = 0

# outputs the first two numbers in the fibonacci sequence
print(first_Position_Fibonacci, end=", ")
print(second_Position_Fibonacci, end =", ")

# to represent the Fibonacci sequence
# the way this for loop works is that it outputs the next number 
# by the sum of the two prior numbers, which initial start from 0 and 1
# In mathemathical terms to show the Fibonacci sequence is 
# F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
for i in range((n-2)):
    sum_Next_Position = first_Position_Fibonacci + second_Position_Fibonacci
    print(sum_Next_Position, end=", ")

    # to show the shift in terms when moving on to the next number
    first_Position_Fibonacci = second_Position_Fibonacci
    second_Position_Fibonacci = sum_Next_Position

