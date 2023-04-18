import numpy as np
from numpy import linalg

# Dante LoPriore
# March 17, 2023
# PS3: Problem 6

# Purpose: to produce a function that allows the user to create a m by n array and 
# prints the diagonal elements with a negative slope that starts from the most top-right entry.

# Examples of How to Initalize a Matrix in Python
matrix2 = np.ndarray(shape=(5,4)) 
matrix4 = np.array([[1, 2, 3], [5, 6, 7], [9, 10, 11]])
matrix5 = np.array([[1, 2], [5, 6], [9, 10]])
matrix3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]])
matrix1 = np.round(np.random.rand(5, 4)*100)
transposed_matrix = np.transpose(matrix3)

# allows the user to input the number of rows an columns for a matrix
m = int(input("Please input the row parameter for the matrix: "))
n = int(input("Please input the column parameter for the matrix: "))

# creates a matrix with a size based on the user's response for n and m
A = np.random.randint(20, size=(m, n))

# outputs the matrix
print("Matrix Before Passed through the method\n")
print(A)
print("Matrix After Passed through the method\n")

# Matrix of Integers -> Integers
# to print the diagonal entries with a negative slope, 
# which starts from the most top-right element
def print_diagonal_entries_with_neg_slope(givenMatrix):
    # initialize row length
    m_row_matrix = len(givenMatrix)
    
    # initialize index to iterate in loop 
    # the index is the length of the (row - 1) since the for loop is going in decending order of indexes.
    cur_index = m_row_matrix-1

    # iterating through the first row's columns in decending order of indexes.
    for cur_index in range(m_row_matrix, 0, -1):

        # outputs the negative slope for just the first row's columns in the matrix 
        # diag uses a key, which is the index of the entry of columns in the first row, 
        # to preform the negative slope action
        print(*np.diag(givenMatrix, k=cur_index))

     # iterating through the remaining rows' first column in acendening order of indexes.
    for index in range(0, m_row_matrix):

        # outputs the negative slope for the remaining rows' based on the first column in the matrix 
        # diag uses a key, which is the index of the entry of first column for the rest of the rows,
        # to preform the negative slope action
        print(*np.diag(givenMatrix, k= (-index)))
    return ""
    
"""
Further Explaination of Function:
I beleived that using diag for the function is more effecient than indexing to preform the task.
Here is a more detailed explaination to my thought process on using the function

Example Matrix 
[[1, 2, 3, 4], 
[5, 6, 7, 8], 
[9, 10, 11, 12], 
[13, 14, 15, 16], 
[17, 18, 19, 20]]

DESCRIPTION FIRST FOR LOOP:

Takes an column from just first row  
Ex: [1, 2, 3, 4]

Gets top-right most by get length of cols which is 4
The starting number is 4 since it is highest column 

Then diagonal function takes the index of a column in the row and performs the negative slope
In: *np.diag(givenMatrix, k=2) which the key is the 3 entry since its index is 2
Out: 3, 8

DESCRIPTION SECOND FOR LOOP:

Takes an first column from the remaining rows which is 
Ex: [5, 9, 13, 17] which has the index of -1

Goes through the loop in acending order
Then diagonal function takes the negative index of the row that the entry or column 
is located in then performs the negative slope
In: *np.diag(givenMatrix, k=-1) which the key is the 5 entry since its index is -1
Out: 5, 10, 15, 20 

"""

print(print_diagonal_entries_with_neg_slope(A))












