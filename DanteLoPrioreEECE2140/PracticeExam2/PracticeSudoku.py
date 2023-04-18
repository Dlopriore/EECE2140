import numpy as np


def isValidSudoku(board):
    unique_numbers_rowwise = dict()
    unique_numbers_columnwise = dict()
    unique_numbers = dict()
    for row in board:
        for col in row:
            if (col not in unique_numbers_rowwise):
                unique_numbers_rowwise.update({str(col): 1})
            else:
                unique_numbers_rowwise[str(col)] += 1
    
    for row in board.T:
        for col in row:
            if (col not in unique_numbers_columnwise):
                unique_numbers_columnwise.update({str(col): 1})
            else:
                unique_numbers_columnwise[str(col)] += 1
        
    for freq_val in unique_numbers_columnwise.values():
        if freq_val > 1:
            return False
    
    for freq_val in unique_numbers_rowwise.values():
        if freq_val > 1:
            return False
    
    for r_index in range(3):
        for col_index in range(3):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
    
    unique_numbers = dict()
    col_index = 3
    for r_index in range(3):
        for col_index in range(6):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
    
    unique_numbers = dict()
    col_index = 6
    for r_index in range(3):
        for col_index in range(9):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
        
    unique_numbers = dict()
    col_index = 6
    for r_index in range(3):
        for col_index in range(9):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
    
    unique_numbers = dict()
    col_index = 0
    r_index = 3
    for r_index in range(6):
        for col_index in range(3):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
        
    unique_numbers = dict()
    col_index = 3
    r_index = 3
    for r_index in range(6):
        for col_index in range(6):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
    
    unique_numbers = dict()
    col_index = 6
    r_index = 3
    for r_index in range(6):
        for col_index in range(9):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
    
    unique_numbers = dict()
    col_index = 0
    r_index = 6
    for r_index in range(9):
        for col_index in range(3):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
    
    unique_numbers = dict()
    col_index = 3
    r_index = 6
    for r_index in range(9):
        for col_index in range(6):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
    
    unique_numbers = dict()
    col_index = 6
    r_index = 6
    for r_index in range(9):
        for col_index in range(9):
            if board[r_index][col_index] in unique_numbers:
                unique_numbers.update({str(board[r_index][col_index]): 1})
            else:
                unique_numbers[str(board[r_index][col_index])] += 1
    
    for freq_val in unique_numbers.values():
        if freq_val > 1:
            return False
    
    return True
    

    

    



        

        
        


inMat = np.array([[6, 3, 9, 5, 7, 4, 1, 8, 2],
                              [5, 4, 1, 8, 2, 9, 3, 7, 6],
                              [7, 8, 2, 6, 1, 3, 9, 5, 4],
                              [1, 9, 8, 4, 6, 7, 5, 2, 3],
                              [3, 6, 5, 9, 8, 2, 4, 1, 7],
                              [4, 2, 7, 1, 3, 5, 8, 6, 9],
                              [9, 5, 6, 7, 4, 8, 2, 3, 1],
                              [8, 1, 3, 2, 9, 6, 7, 4, 5],
[2, 7, 4, 3, 5, 1, 6, 9, 8]])

print(isValidSudoku(inMat))