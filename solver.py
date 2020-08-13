import numpy as np

def is_valid(board, number, x, y):
    """[summary]

    Args:
        board (int[][]): [description]
        number (int): [description]
        x (int): [description]
        y (int): [description]
    """

    # check if number already exists in row
    if number in board[y]:
        return False

    # check if number already exists in col
    if number in [board[i][x] for i in range(9)]:
        return False

    subgrid_x = x // 3
    subgrid_y = y // 3

    # check if number exists in a 3x3 subgrid
    if number in [board[i][j] for i in range(subgrid_y * 3, subgrid_y * 3 + 3) for j in range(subgrid_x * 3, subgrid_x * 3 + 3)]:
        return False

    return True

def get_unassigned_cell(board):
    """[summary]

    Args:
        board ([type]): [description]

    Returns:
        [type]: [description]
    """
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0:
                return x, y
    return None


def solve(board, gui=False):
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
            board[y][x] = num
            if solve(board):
                return True
            board[y][x] = 0
    return False

