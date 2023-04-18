import numpy as np
import matplotlib.pyplot as plt

def find_common_elements(matrix):
    # initialize a set with the elements of the first row of the matrix
    common_elements = set(matrix[0])

    # iterate through the rest of the rows of the matrix
    for row in matrix[1:]:
        # update the common_elements set with the intersection of the current row and the previous common_elements set
        common_elements = common_elements.intersection(row)

    # return the sorted list of common elements
    return sorted(common_elements)


matrix = np.array([[7, 1, 5, 6], [2, 6, 1, 1], [6, 1, 9, 2], [6, 6, 3, 1], [5, 5, 6, 1], [3, 6, 7, 1]])

transposed_matrix = matrix.transpose()

common_elements = find_common_elements(transposed_matrix)

print(common_elements)



