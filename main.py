import argparse
from solver import solve

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

def print_board(board):
    """[summary]

    Args:
        board ([type]): [description]
    """
    board_print = '\n'.join([''.join(['{:3}'.format(val) for val in row]) for row in board])
    print(board_print)

def solve_text(board):
    print("Starting board: ")
    print_board(board)

def main(gui):
    solved = solve(board, gui)
    
    if gui:
        pass
    else:
        if solved:
            print("Successully solved sudoku!")
            print_board(board)
        else:
            print("Couldn't solve the puzzle.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program solves sudokus.')
    parser.add_argument('--gui', action='store_true', help='Run the program with a nice GUI')
    args = parser.parse_args()

    main(args.gui)
