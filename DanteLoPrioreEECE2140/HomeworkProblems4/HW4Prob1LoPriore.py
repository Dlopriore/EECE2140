import numpy as np
from numpy import linalg

# Dante LoPriore
# March 28, 2023
# PS4: Problem 1

# Purpose: to produce a function that gets a matrix and prints the elements 
# that are common seen in the rows of the matrix.

# to input the number of rows and columns for a matrix
m = int(input("Please input how many rows for the matrix: "))
n = int(input("Please input how many column for the matrix: "))

# creates a matrix with a size based on the user's response for n and m
A = np.random.randint(10, size=(m, n))

# allows user to decide which axis to check the common elements
desired_axis = int(input("Please input axis type (0 for row-wise / 1 for column-wise): "))

# Matrix of Integers -> Set of Integers
# to determine whether to produce the common elements of a matrix row-wise or column-wise
def produce_common_elements(given_Matrix, axis_type=0):
    if (axis_type == 0): 
        return find_commmon_elements(given_Matrix)
    else: 
        return find_commmon_elements(given_Matrix.transpose())


# Matrix of Integers -> Set of Integers
# to find the common elements of a given matrix by taking the interesection of each row 
# to find the unique integers or enteries in the matrix
def find_commmon_elements(given_Matrix):

    known_common_elements = set(given_Matrix[0])

    #iterates throught each row in the matrix 
    for index in range(1, len(given_Matrix)):

        # stores only unique items and no duplicates through comparing two sets
        # by taking the intersection of a set of the first row and a set of the next row
        next_row_matrix = set(given_Matrix[index])
        known_common_elements = known_common_elements.intersection(next_row_matrix)
    
    # to output the common elements
    return known_common_elements

# allows user to see the desired m by n matrix 
print("Matrix Before Entering the Method: ")
print(A)
print("")

print("Matrix's Common Elements After Entering the Method: ")
print(produce_common_elements(A, axis_type=desired_axis))
#print(find_commmon_elements(A))

#A = np.array([[7, 1, 5, 6], [2, 6, 1, 1], [6, 1, 9, 2], [6, 6, 3, 1], [5, 5, 6, 1], [3, 6, 7, 1]])
#print(find_commmon_elements(A.T))







