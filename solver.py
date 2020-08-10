import numpy as np


def is_valid(board, number, x, y):
    """[summary]

    Args:
        board ([type]): [description]
        number ([type]): [description]
        x ([type]): [description]
        y ([type]): [description]
    """

    # check if number already exists in row
    if number in board[x]:
        return False

    # check if number already exists in col
    if number in [board[i][y] for i in range(9)]:
        return False

    # check if number exists in a 3x3 subgrid
    for i in range(6,7,8):
        for j in range(3,4,5):
            pass 

def get_unassigned_cell(board):
    """[summary]

    Args:
        board ([type]): [description]

    Returns:
        [type]: [description]
    """
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                return x, y
    return None


def solve(board):
    """[summary]

    Args:
        board ([type]): [description]

    Returns:
        [type]: [description]
    """

    x, y = get_unassigned_cell(board) or (None, None)
    if x is None or y is None:
        return True
    
    for num in range(1,10):
        if is_valid(board, num, x, y):
            board[x][y] = num
            if solve(board):
                return True
            board[x][y] = 0
    return False

def print_board(board):
    """[summary]

    Args:
        board ([type]): [description]
    """
    board_print = '\n'.join([''.join(['{:3}'.format(val) for val in row]) for row in board])
    print(board_print)

if __name__ == "__main__":

    board = [ 
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

    print("Input: ")
    print_board(board)
    if solve(board):
        print("Successully solved sudoku!")
        print_board(board)
