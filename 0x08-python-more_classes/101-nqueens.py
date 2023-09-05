#!/usr/bin/python3
"""
N-Queens backtracking program to print the coordinates of N queens
on an NxN grid such that they are all in non-attacking positions.
"""

import sys

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def print_usage():
    print("Usage: nqueens N")

def initialize_board(size):
    return [[row, None] for row in range(size)]

def does_queen_exist_in_column(board, column, y):
    for row in range(len(board)):
        if y == board[row][column]:
            return True
    return False

def is_safe(board, row, column, y):
    if does_queen_exist_in_column(board, column, y):
        return False

    for i in range(row):
        if abs(board[i][column] - y) == abs(i - row):
            return False

    return True

def clear_board_from_index(board, index):
    for i in range(index, len(board)):
        board[i][1] = None

def solve_nqueens(board, size, row=0):
    if row == size:
        print(board)
        return

    for y in range(size):
        clear_board_from_index(board, row)
        if is_safe(board, row, 1, y):
            board[row][1] = y
            solve_nqueens(board, size, row + 1)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not is_integer(sys.argv[1]):
        print_usage()
        sys.exit(1)

    n = int(sys.argv[1])

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_board(n)
    solve_nqueens(chessboard, n)
