# Dante LoPriore
# January 31, 2023
# PS2: Problem 2

# Purpose: to create a function that calculates the 
# sum and min value or product and max value for a list of integers 
# based on the user's input

# [Int] Int -> Str Str
# to compute sum and min value or product and max value for a list of integers 
# the functions is set at a default value of 0 which will caluculate the min and sum
def sum_product(*given_list_of_integers, in_mode=0):

    # initialize the variables for the product and the sum 
    sum_of_elements = 0
    product_of_elements = 0
    minimium_number_in_list = 0
    maximium_number_in_list = 0

    # to determine whether the mode is set on the default and 
    # understand which path of computations it should preform
    if (in_mode == 0):

        # computes the minimum value seen in the list.
        minimium_number_in_list = min(*given_list_of_integers)

        # computes the sum of all the elements in the list
        sum_of_elements += sum(given_list_of_integers)

        return (f'The minimium result is {minimium_number_in_list}', f'The sum of the result is {sum_of_elements}') #packing
    else:

        # computes the maximum value seen in the list.
        maximium_number_in_list = max(given_list_of_integers)

        # computes the product by extracting every element in a list and 
        # then multiplying each element until the list is empty.
        for i in range(0,len(given_list_of_integers)):
            if (i == 0):
                product_of_elements = given_list_of_integers[i]
            else:
                product_of_elements *= given_list_of_integers[i]
        return (f'The maximium result is {maximium_number_in_list}', f'The product of the result is {product_of_elements}') #packing


my_list = [8, 9, 3, 4, 5, 6, 7]

# to initialize the variables for the two outputs from the function
min_or_max_result, sum_or_product_result = sum_product(*my_list, in_mode=1)

# to outpute the results from the function
print(min_or_max_result)
print(sum_or_product_result)

# test default
min_or_max_result, sum_or_product_result = sum_product(8, 9, 3, 4, 5, 6, 7)

# to outpute the results from the function
print(min_or_max_result)
print(sum_or_product_result)

# test default in parameter of function
min_or_max_result, sum_or_product_result = sum_product(*my_list)

# to outpute the results from the function
print(min_or_max_result)
print(sum_or_product_result)

