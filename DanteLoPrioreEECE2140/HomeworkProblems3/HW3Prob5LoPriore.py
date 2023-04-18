import numpy as np
from numpy import linalg

# Dante LoPriore
# March 25, 2023
# PS3: Problem 5

# Purpose: to preform math operations on two matrixs

# Task 1
# Create a 3x3 array A that has even integers from 2 to 18. 
# Create a 3x3 array B that has the integers from 9 to 1.
A = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Task 2
# Raise each element of A by 2 
A **= 2
print("Raise each element of A by 2 ")
print(A)
print("")


# Task 3 
# Multiply A using the second array elementwise and matrix-wise

A_B_mult = np.dot(A, B)
# Element-Wise Multiplcation
print("Element-Wise Multiplcation")
print(A_B_mult)
print("")

# Matrix-wise Multiplcation
print("Matrix-wise Multiplcation")
print(np.multiply(A, B))
print("")

# Task 4
# Replace elements of A and B, where 
# B -> A has negative for multiple integer of 4
# A -> B has multiple integers of 3 with a square root value
# To complete the task boolean logic indexing is required

A[B % 3] = np.sqrt(A[B % 3])
B[A % 4] = -B[A % 4] 

print("Replaced Elements for A")
print(A)
print("")

print("Replaced Elements for B")
print(B)
print("")

# Task 4
# Multiply the inverse matrix of the first multiplication of A and B 
# to the inverise of the new A and elementwise and matrix-wise.

inv_previous_AB = np.linalg.inv(A_B_mult)
inv_new_AB = np.linalg.inv(np.dot(A, B))

print('Multiplication of the Two Inverse Matrix Element-Wise')
print(np.dot(inv_previous_AB, inv_new_AB))
print("")

print('Multiplication of the Two Inverse Matrix Matrix-Wise')
print(np.multiply(inv_previous_AB, inv_new_AB))
