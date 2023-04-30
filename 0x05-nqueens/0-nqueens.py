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
        if board[i] == row or \
           board[i] == row - col + i or \
           board[i] == row + col - i:
            return False

    return True

def solve_n_queens(n, board, col, solutions):
    if col == n:
        solutions.append(board[:])
        return

    for row in range(n):
        if is_valid(board, row, col):
            board[col] = row
            solve_n_queens(n, board, col+1, solutions)

def n_queens():
    """
    Returns a list of lists
    containing the [row,col]
    with the queen given n values
    """
    solutions = []
    
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
        
    board = [-1] * n
    solve_n_queens(n, board, 0, solutions)

    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])

if __name__ == '__main__':
    n_queens()