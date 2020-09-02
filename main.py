import argparse
from solver import SudokuSolver
from tkinter import *
import tkinter.font as tkFont
import numpy as np
import threading
import copy


class SudokuSolverGUI(Frame):

    WIDTH = 720
    HEIGHT = 480

    def __init__(self, board, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.original_board = copy.deepcopy(board)
        self.board = board
        self.solver = SudokuSolver()
        self.entries = []
        self._grid = []
        self.customFont = tkFont.Font(family="Helvetica", size=16)
        self.master.wm_title("Sudoku Solver")
        self.master.geometry("{}x{}".format(self.WIDTH, self.HEIGHT))

        self._init_widgets()

        self.__update_job = None

        self.pack(fill=BOTH, expand=1)


    def update_entries(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.entries[i][j].set(self.board[i][j] if self.board[i][j] else '')
        self.master.update()

    def _cancel_update(self):
        self.master.after_cancel(self.__update_job)

    def _init_widgets(self):

        grid = Frame(self, background="black")
        grid.pack()

        self._create_grid(grid)

        messageBox = Frame(self)
        messageBox.pack(padx=5, pady = 10)

        self.message = StringVar()
        messageLabel = Label(messageBox, textvariable=self.message, font=self.customFont)
        messageLabel.pack()

        buttons = Frame(self)
        buttons.pack(padx=10, pady=10)

        solveButton = Button(buttons, text="Solve", command=self.solve, font=self.customFont)
        solveButton.pack(side=LEFT)

        checkButton = Button(buttons, text="Check", command=self.check, font=self.customFont)
        checkButton.pack(side=LEFT)

        resetButton = Button(buttons, text="Reset", command=self._reset_board, font=self.customFont)
        resetButton.pack(side=LEFT)

        exitButton = Button(buttons, text="Exit", command=self.exitApp, font=self.customFont)
        exitButton.pack(side=RIGHT)

    def _create_grid(self, grid):

        self._grid = np.zeros((9,9), dtype=object)
        self.entries = np.zeros((9,9), dtype=object)

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                var = StringVar()
                if self.board[i][j] == 0:
                    vcmd = (self.register(self._validate_entry), '%s', '%S', '%d', '%W', '%P')
                    self._grid[i][j] = Entry(grid, textvariable=var,width=3, relief=FLAT,
                                            font=self.customFont, validate='key', validatecommand=vcmd)
                    self._grid[i][j].grid(
                        row=i, column=j, padx=1, pady=1)
                else:
                    var.set(self.board[i][j])
                    self._grid[i][j] = Label(grid, textvariable=var, width=3, font=self.customFont, relief=FLAT)
                    self._grid[i][j].grid(
                        row=i, column=j, padx=1, pady=1)
                self.entries[i][j] = var


    def _validate_entry(self, s, S, d, W, P):
        action = int(d)
        if action == 1:
            return len(s) == 0 and S.isnumeric() and 1 <= int(S) <= 9
        
        if action == 0:
            entry = self.master.nametowidget(W)
            entry['background'] = 'Red'
            entry['foreground'] = 'White'
            return True

    def _disable_entry_fields(self, disabled):
        for row in self._grid:
            for entry in row:
                entry['state'] = 'disabled' if disabled else 'normal'

    def solve(self): 
        self._disable_entry_fields(True)
        t = threading.Thread(target=self.solver.solve, kwargs={'board': self.board})
        self.__update_job = self.master.after(100, self.update_entries)
        t.start()
    
    def _is_finished(self):
        for col in self.board:
            for val in col:
                if not val:
                    return False
        return True

    def check(self):
        if self._check_solution():
            self.message.set("Congratulations! You have successfully solved the sudoku!")
        else:
            self.message.set("Try again! You can reset or make changes to your current solution.")

    def _reset_board(self):
        if self.__update_job:
            self._cancel_update()
        self._disable_entry_fields(False)
        self.message.set("")
        self.board = copy.deepcopy(self.original_board)
        self.update_entries()
    
    def _check_solution(self):
        if not self._is_finished():
            return False

        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                val = self.board[y][x]
                if not self.solver._is_valid(self.board, val, x, y):
                    return False
        return True


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

    solver = SudokuSolver(board)

    if gui:
        root = Tk()
        app = SudokuSolverGUI(board, root)
        app.mainloop()
    else:
        if solver.solve():
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
