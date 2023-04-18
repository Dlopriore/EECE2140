import numpy as np


# Dante LoPriore 
# April, 11, 2022
# Exam 2 Problem 1

# to determine whether the given matrix is a valid square 
# and define what type of magic square
# Matrix of Integers -> (Bool, Integer)
def is_magic(givenMat):
    if (valid_normal_magic_square(givenMat)):
        return (True, 0) 
    if ((check_semi_magic_square(givenMat))):
        return (True, 2)
    if (check_trival_magic_square(givenMat)):
        return (False, 1)
    else:
        return (False, -1)


# to check if the given matrix is a valid normal magic square
# # Matrix of Integers -> (Integer)
def valid_normal_magic_square(givenMat):

    sum_diagonals_given_mat_positive_slope = np.trace(givenMat)
    neg_slope = []
    i=0
    for r_index in range(len(givenMat[0])-1, -1, -1):
        neg_slope.append(givenMat[i][r_index])
        i+=1
    sum_diagonals_given_mat_negative_slope = np.sum(neg_slope)
    sum_equal_overall_in_mat = True 

    # Checks if each row is negative
    for row in givenMat:
        for col in row:
            if(col < 0):
                return False

    #Checks row-wise
    for row in givenMat:
        if((sum(row) == sum_diagonals_given_mat_positive_slope) and (sum_diagonals_given_mat_positive_slope == sum_diagonals_given_mat_negative_slope)):
            pass
        else:
            return False
    
    #Checks column-wise
    for row in givenMat.T:
        if((sum(row) == sum_diagonals_given_mat_positive_slope) and (sum_diagonals_given_mat_positive_slope == sum_diagonals_given_mat_negative_slope)):
            pass
        else:
            return False
    
    return sum_equal_overall_in_mat

# to check if the given matrix is a valid trival magic square
# by checking duplicates
# Matrix of Integers -> bool
def check_trival_magic_square(givenMat):
    freq_dict = dict()
    is_valid_trival = False
    for row in givenMat:
        for col in row:
            if(col not in freq_dict.keys()):
                freq_dict.update({col: 1})
            else:
                freq_dict[col] += 1
    
    for entry_value_freq in freq_dict.values():
        if (entry_value_freq > 1):
            return True
    
    return is_valid_trival

# to check if the given matrix is a valid semi magic square
# Matrix of Integers -> bool 
def check_semi_magic_square(givenMat):

    neg_slope = []
    sum_diagonals_given_mat_positive_slope = np.trace(givenMat)
    i=0
    for r_index in range(len(givenMat[0])-1, -1, -1):
        neg_slope.append(givenMat[i][r_index])
        i+=1

    sum_diagonals_given_mat_negative_slope = np.sum(neg_slope)

    in_row_sum_list = list()
    in_col_sum_list = list()

    # Checks if each row is negative
    for row in givenMat:
        for col in row:
            if(col < 0):
                return False 

    #Checks row-wise
    for row in givenMat:
        in_row_sum_list.append(sum(row))
    
    #Checks column-wise
    for row in givenMat.T:
        in_col_sum_list.append(sum(row))
    
    if (sum_diagonals_given_mat_positive_slope == sum_diagonals_given_mat_negative_slope):
        return False
    
    #Check if the sum of the rows and columns equal each other
    for k in range(len(givenMat[0])):
        if ((in_row_sum_list[k] != in_col_sum_list[k])):
            return False
    return True

in_mat = np.array([[2, 16, 13, 3],
  [11, 5, 8, 10],
  [7, 9, 12, 6],
  [14, 4, 1, 15]])

in_mat_known_square = np.array([[29**2, 1**2, 47**2],
  [41**2, 7**2, 1**2],
  [23**2, 41**2, 29**2]])

print(is_magic(in_mat))
print(is_magic(in_mat_known_square))


