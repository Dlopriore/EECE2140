A = [[3, 6, -4, 6], [-8, -4, -1, -7], [-5, 3, -1, 9]] 

def sort_matrix(inMat, modeSelect=0):
    if modeSelect == 0:
        # return a sorted list of values in each row in acending order
        return [sorted(row) for row in inMat]
    elif modeSelect == 1:
        # return a sorted list of values in each row in decending order
        sorted_list_reverse_order = [sorted(row, reverse=True) for row in inMat]
        
        # return a sorted list of values in each row in decending order
        # the function returns a list where each column of the input matrix in_mat is sorted in the descending order.
        num_cols = len(sorted_list_reverse_order[0])
        max_value = 0
        high_values = []
        for col in range(num_cols):
            max_val = inMat[0][col]
            for row in range(1, len(sorted_list_reverse_order)):
                if inMat[0][col] > max_value:
                    max_value = inMat[0][col]
            high_values.append(max_val)
        return high_values

print(sort_matrix(A, modeSelect=0))
print(sort_matrix(A, modeSelect=1))
