# Dante LoPriore
# March 17, 2023
# PS3: Problem 3

# Purpose: to produce a function that allows a user to enter mathematical word problems and
# computes the final computation by using string processing, which will distinguish the numbers and operators.

# allows user to input a mathematical word problem
user_response_mathematical_word_problem = input("Please enter a mathematical word problem: ")

# String -> Integer
# to produce the final answer of the mathematical word problems using string processing, 
# which will distinguish the numbers and operators.
def solve_mathematical_word_problem(given_mathematical_word_problem):

    # initalize variables to store the numbers and final answer
    number1 = 0 
    number2 = 0
    final_result = 0

    # to determine whether the operator in the math problem uses two words
    if(("divided by" in given_mathematical_word_problem) or ("raised to" in given_mathematical_word_problem)):
        math_operation = ''

        # to split up each word into a list by using the spacing as it will tokenize the phrase into words
        individiual_item_list = given_mathematical_word_problem.split(" ")

        # to remove additional spaces in the phrase
        individiual_item_list = [mem for mem in individiual_item_list if mem]

        # to store the identified math operation and concatinate the two words together
        math_operation += individiual_item_list[1] + " "
        math_operation += individiual_item_list[2]

        # to convert the string number as an integer
        number1 = get_number(individiual_item_list[0])
        number2 = get_number(individiual_item_list[3])

        # preform math operations with given integer numbers
        if(math_operation in "divided by"): final_result = number1 / number2
        if(math_operation in "raised to"): final_result = number1 ** number2

    else:
        # to split up each word into a list by using the spacing as it will tokenize the phrase into words
        individiual_item_list = given_mathematical_word_problem.split(" ")

        # to remove additional spaces in the phrase
        individiual_item_list = [mem for mem in individiual_item_list if mem]

        # to convert the string number as an integer
        number1 = get_number(individiual_item_list[0])
        number2 = get_number(individiual_item_list[2])

        # preform math operations with given integer numbers
        if(individiual_item_list[1] in "plus"): final_result = number1 + number2
        if(individiual_item_list[1] in "minus"): final_result = number1 - number2
        if(individiual_item_list[1] in "times"): final_result = number1 * number2
    
    # output final result
    return final_result


# String -> Integer
# to produce the string number word word into the integer value of that number
def get_number(given_item):
    number = 0
    if (given_item in 'zero'): number = 0
    if (given_item in 'one'): number = 1 
    if (given_item in 'two'): number = 2
    if (given_item in 'three'): number = 3
    if (given_item in 'four'): number = 4
    if (given_item in 'five'): number = 5
    if (given_item in 'six'): number = 6
    if (given_item in 'seven'): number = 7
    if (given_item in 'eight'): number = 8
    if (given_item in 'nine'): number = 9
    return number
    
# prints the output of the math problem
print(solve_mathematical_word_problem(user_response_mathematical_word_problem))
    
