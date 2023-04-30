#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard
"""
import sys

def is_valid(board, row, col):
    """
    Checking if two queens are in the same position
    Check diagonally to the left
    Lower diagonal
    """

    for i in range(col):
        if board[row][i] == 1:
            return False
    #Check diagonally to the left 
    k = row
    j = col
    while k >= 0 and j >= 0:
        if board[k][j] == 1:
            return False
        k -= 1
        j -= 1

    k = row
    j = col
    #Lower diagonal
    while k < len(board) and j > col > 0:
        if board[k][j] == 1:
            return False
        k += 1
        j -= 1
    return True

def chess():
    """
    Returns an list of lists 
    containing the [row,col]
    with the queen given n values
    """
    solution = []
    nqueens = [] #Already placed queens
    row, col = 0
    n = sys.argv[2]
    
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
        
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for _ in range(n):
        if is_valid(nqueens, row, col):
            nqueens.append(row, col)
        return solution.append(nqueens)

if __name__ == '__main__':
    chess()
    
    
    

    
    

    



