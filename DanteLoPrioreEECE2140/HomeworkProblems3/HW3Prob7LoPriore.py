import numpy as np
from numpy import linalg

# Dante LoPriore
# March 23, 2023
# PS3: Problem 7

# Purpose: to produce a function that determines the mean and mode of a whole matrix and 
# then complete the computation row-wise and column-wise

matrix1 = np.array([[1, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [2, 1, 2, 16]])
matrix4 = np.array([[1, 2, 3], [5, 6, 7], [9, 10, 11]])
matrix12 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [13, 14, 15, 16]])
matrix3 = np.array([[1, 1, 1, 1], [9, 1, 1, 8], [9, 10, 98, 0], [13, 14, 15, 16], [0, 0, 151, 16]])
A = np.random.randint(20, size=(5, 5))
B = np.random.randint(20, size=(2, 3))
C = np.random.randint(20, size=(6, 4))

# Completes Part A Requirement

# Matrix of Integers -> Integer
# to produce the mode of a whole matrix 
def solve_whole_matrix_mode(user_repsonse_matrix):

    # initialize varaiables to store collection of entries and frenquecy amounts
    item_frequency = dict()
    greatest_frenquecy_amount = 0
    final_mode_result = []

    # to iterate over all the entries in the matrix and create a dictionary that 
    # used the value of the entries as the key and the occurences of that entry as the value.
    for row in user_repsonse_matrix:
        for col in row:
            if(col in item_frequency.keys()): item_frequency[col] += 1
            else: item_frequency.update({col: 1})
    
    # to determine the max frequency seen in the matrix
    for freq_value in item_frequency.values():

        # to determine that frequency in the dictionary is the greatest
        if freq_value >= greatest_frenquecy_amount: greatest_frenquecy_amount = freq_value
    
    # iterates through each entry to determine whether that the entry contains the greatest frequency
    final_mode_result = [key_item for key_item in item_frequency.keys() if item_frequency[key_item] == greatest_frenquecy_amount and (greatest_frenquecy_amount != 1)]

    # to output the final result for the mode
    return final_mode_result

# Matrix of Integers -> Integers
# to produce the median of a whole matrix 
def solve_whole_matrix_median(user_repsonse_matrix):

    #initialize the varaiables to store the data from the matrix 
    row_wise_matrix_list = []

    # iterates through each entry in the matrix and stores each entry 
    # into a single list that has one row
    for row in user_repsonse_matrix:
        for col in row:
            row_wise_matrix_list.append(col)

    # sorted list in accending numerical order
    row_wise_matrix_list.sort()
    
    # to determine whether the amount of entries in the matrix are even or odd since 
    # the computation for these cases are different 
    if(len(row_wise_matrix_list) % 2 == 0):
        # Even Number of Entries Case:

        # finds the two middle entries of the list 
        # by getting the index towards the middle of the list
        index_median1 = int(len(row_wise_matrix_list) //2)
        index_median2 = int(len(row_wise_matrix_list) //2)-1
        median_calc_1 = row_wise_matrix_list[index_median1]
        median_calc_2 = row_wise_matrix_list[index_median2]

        # outputs the median by computing the average of the two median calculations
        return (median_calc_1 + median_calc_2)/2
    else:
        # Odd Number of Entries Case:

        # finds the middle entry of the list by getting middle index of the list
        index_median = int(len(row_wise_matrix_list) //2)

        # outputs the median of the matrix
        return row_wise_matrix_list[index_median]
    

# Completes Part B Requirement

# allows user to chose if the want the calulcations of the mode and median row-wise or column-wise
user_desired_axis = int(input("Would you like to preform the mode or median of the matrix row-wise or column-wise (0 for row-wise / 1 for column-wise)"))

# Matrix of Integers -> List of Integers
# to produce the mode and median row-wise or column-wise
def determine_matrix_mode_and_median(givenMatrix, axis_mode=0):

    # to determine whether it should be row-wise or column wise
    if axis_mode == 0:
        return f'The mode of the matrix row-wise is {compute_matrix_mode(givenMatrix)} \n\
            The median of the matrix row-wise is {compute_matrix_median(givenMatrix)}'
    else:
        return f'The mode of the matrix column-wise is {compute_matrix_mode(givenMatrix.transpose())} \n\
            The median of the matrix column-wise is {compute_matrix_median(givenMatrix.transpose())}'


# Matrix of Integers -> List of Integers
# to produce the mode of each rows in a matrix 
def compute_matrix_mode(user_repsonse_matrix):

    # iterates through each row of the matrix to perform the mode calculation
    final_mode_result = []
    final_mode_result = [produce_mode(row) for row in user_repsonse_matrix]

    # outputs the final mode calculations for all rows
    return final_mode_result

# List of Integers -> [Integer]
# to produce the mode of a single row in a matrix 
def produce_mode(given_matrix_row):
    
    # initialize varaiables to store collection of entries and frenquecy amounts
    item_frequency = dict()
    most_frequent = 0

    # to iterate over all the entries in the row and create a dictionary that 
    # used the value of the entries as the key and the occurences of that entry as the value.
    for col in given_matrix_row:
            if(col in item_frequency.keys()): item_frequency[col] += 1
            else: item_frequency.update({col: 1})
    
    # to determine the max frequency seen in the matrix
    for freq_value in item_frequency.values(): 

        # to determine that frequency in the dictionary is the greatest
        if freq_value >= most_frequent: most_frequent = freq_value
    
    # iterates through each entry to determine whether that the entry contains the greatest frequency
    final_mode_result = [key_item for key_item in item_frequency.keys() if item_frequency[key_item] == most_frequent and (most_frequent != 1)]

    # to output the final result for the mode
    return final_mode_result


# Matrix of Integers -> List of Integers
# to produce the mode of each row in a matrix 
def compute_matrix_median(user_repsonse_matrix):

    # iterates through each row of the matrix to perform the median calculation
    final_result = []
    final_result = [produce_median(row) for row in user_repsonse_matrix]
    return final_result


# List of Integers -> [Integer]
# to produce the mode of a single row in a matrix 
def produce_median(given_matrix_row):

    # iterates through each entry in the matrix and stores each entry 
    # into a single list that has one row
    row_wise_matrix_list = [] 
    for col in given_matrix_row:
        row_wise_matrix_list.append(col)

    # sorted list in accending numerical order
    row_wise_matrix_list.sort()

    # to determine whether the amount of entries in the matrix are even or odd 
    if(len(row_wise_matrix_list) % 2 == 0):

        # finds the two middle entries of the list 
        # by getting the index towards the middle of the list
        index_median1 = int(len(row_wise_matrix_list) //2)
        index_median2 = int(len(row_wise_matrix_list) //2)-1
        median_calc_1 = row_wise_matrix_list[index_median1]
        median_calc_2 = row_wise_matrix_list[index_median2]

        # outputs the median by computing the average of the two median calculations
        return (median_calc_1 + median_calc_2)/2
    else:

        # finds the middle entry of the list by getting middle index of the list
        index_median = int(len(row_wise_matrix_list) //2)
        return row_wise_matrix_list[index_median]


#print(compute_matrix_mode(matrix1)) #row wise
#print(compute_matrix_mode(matrix1.transpose())) #column wise 

#print(compute_matrix_median(matrix4))
#print(compute_matrix_median(matrix4.transpose()))

#print(solve_whole_matrix_median(matrix3))
#print(solve_whole_matrix_mode(matrix3))
print(determine_matrix_mode_and_median(matrix3, axis_mode=user_desired_axis))

