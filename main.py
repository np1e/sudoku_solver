import argparse
from solver import solve
from tkinter import *


class SudokuSolver(Frame):

    WIDTH = 720
    HEIGHT = 480

    def __init__(self, board, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.wm_title("Sudoku Solver")
        master.geometry("{}x{}".format(self.WIDTH, self.HEIGHT))

        sel.board = board
        self.pack(fill=BOTH, expand=1)

        self._init_widgets()

    def _init_widgets(self):

        grid = Frame(self.master, relief='sunken')
        self._create_grid(grid)

        grid.pack(side=TOP)

        buttons = Frame(self.master, borderwidth=2)
        buttons.pack(side=BOTTOM, padx=10, pady=10)

        exitButton = Button(buttons, text="Exit", command=self.exitApp)
        exitButton.pack(side=RIGHT)

    def _create_grid(self, grid):

        self._grid = []

        for i in self.board:
            for j in self.board[i]:
                if board[i][j] == 0:
                    self._grid[i][j] = Entry(grid, self.board[i][j]).grid(
                        row=i, column=j, padx=3, pady=3)
                else:
                    self._grid[i][j] = Label(grid, text=self.board[i][j]).grid(
                        row=i, column=j, padx=3, pady=3)

    def solve(self):
        pass

    def check(self):
        pass

    def exitApp(self):
        exit()


board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def print_board(board):
    """[summary]

    Args:
        board ([type]): [description]
    """
    board_print = '\n'.join(
        [''.join(['{:3}'.format(val) for val in row]) for row in board])
    print(board_print)


def solve_text(board):
    print("Starting board: ")
    print_board(board)


def main(gui):
    solved = solve(board, gui)

    if gui:
        root = Tk()
        app = SudokuSolver(root, board)
        root.mainloop()
    else:
        pass
        if solved:
            print("Successully solved sudoku!")
            print_board(board)
        else:
            print("Couldn't solve the puzzle.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This program solves sudokus.')
    parser.add_argument('--gui', action='store_true',
                        help='Run the program with a nice GUI')
    args = parser.parse_args()

    main(args.gui)
