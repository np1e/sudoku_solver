import sys
try:
    from tkinter import *
    import tkinter.font as tkFont   
except ImportError:
    from Tkinter import *
    import tkFont

import threading
import copy

class SudokuGrid(Frame):

    UPDATE = 20

    def __init__(self, parent, board, changes, N = 9):
        Frame.__init__(self, parent, bg='Black')
        self.parent = parent
        self.board = board
        self._grid = []
        self._values = []
        self.size = N
        self.changes = changes

        self._create_grid()

        self.__update_job = self.after(0, self._update_grid)
        self.pack()

    def disable(self, disable):
        for row in self._grid:
            for entry in row:
                entry['state'] = 'disabled' if disable else 'normal'

    def _update_grid(self, reset=False):
        if reset:
            for i in range(self.size):
                for j in range(self.size):
                    self._values[i][j].set(self.board[i][j] if self.board[i][j] != 0 else '')
        else:
            if not self.changes.empty():
                if self.parent.visualize.get():
                    change = self.changes.get()
                    self._apply_change(change)
                else:
                    while not self.changes.empty():
                        change = self.changes.get()
                        self._apply_change(change)            

            self.__update_job = self.after(self.UPDATE, self._update_grid)

    def _apply_change(self, change):
        num = change.new_value if change.new_value != 0 else ''
        self._values[change.y][change.x].set(num)

    def reset(self):
        self.after_cancel(self.__update_job)
        self._update_grid(reset=True)

    def _create_grid(self):

        for i in range(self.size):
            self._grid.append([])
            self._values.append([])

            for j in range(self.size):
                var = StringVar()
                if self.board[i][j] == 0:
                    vcmd = (self.register(self._validate_entry), '%s', '%S', '%d', '%W', '%P')
                    self._grid[i].append(Entry(self, textvariable=var,width=2, relief=FLAT,
                                            font=self.parent.customFont, validate='key', validatecommand=vcmd))
                    self._grid[i][j].grid(
                        row=i, column=j, padx=1, pady=1)
                else:
                    var.set(self.board[i][j])
                    self._grid[i].append(Label(self, textvariable=var, width=2, font=self.parent.customFont))
                    self._grid[i][j].grid(
                        row=i, column=j, padx=1, pady=1)

                self._values[i].append(var)
    
    def _validate_entry(self, s, S, d, W, P):
        action = int(d)
        if action == 1:
            return len(s) == 0 and S.isnumeric() and 1 <= int(S) <= 9

class SudokuSolverGUI(Frame):

    WIDTH = 720
    HEIGHT = 480

    def __init__(self, sudoku_solver):
        # set up the Tkinter root window
        self.master = Tk()
        Frame.__init__(self, self.master)

        self.solver = sudoku_solver
        self.board = self.solver.board
        self.original_board = copy.deepcopy(self.board)
        self.customFont = tkFont.Font(family="Helvetica", size=16)
        self.master.wm_title("Sudoku Solver")
        self.master.geometry("{}x{}".format(self.WIDTH, self.HEIGHT))
        self.visualize = BooleanVar()
        self._init_widgets()

        self.pack(fill=BOTH, expand=1)

    def run(self):
        self.master.mainloop()

    def update_model(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = self.grid._values[i][j].get() if self.grid._values[i][j].get().isnumeric() else 0

    def _init_widgets(self):

        self.grid = SudokuGrid(self, self.board, self.solver._changes)

        self.messageBox = Frame(self)

        self.message = StringVar()
        messageLabel = Label(self.messageBox, textvariable=self.message, font=self.customFont)
        messageLabel.pack()

        self._create_buttons()

    def _create_buttons(self):
        self.buttons = Frame(self)
        self.buttons.pack(padx=10, pady=10)

        solveBox = Frame(self.buttons)
        solveBox.pack(side=TOP)

        visualizeButton = Checkbutton(solveBox, text='Visualize', variable=self.visualize, font=self.customFont)
        visualizeButton.pack(side=RIGHT)

        solveButton = Button(solveBox, text="Solve", command=self.solve, font=self.customFont)
        solveButton.pack(side=LEFT)

        checkButton = Button(self.buttons, text="Check", command=self.check, font=self.customFont)
        checkButton.pack(side=LEFT)

        resetButton = Button(self.buttons, text="Reset", command=self._reset_board, font=self.customFont)
        resetButton.pack(side=LEFT)

        exitButton = Button(self.buttons, text="Exit", command=self.exitApp, font=self.customFont)
        exitButton.pack(side=RIGHT)

    def _show_message(self, message):
        self.message.set(message)
        self.messageBox.pack(padx=5, pady = 10)

    def _hide_message(self):
        self.messageBox.pack_forget()    

    def solve(self): 
        self.grid.disable(True)
        self.solver.board = self.board
        t = threading.Thread(target=self.solver.solve)
        t.start()

    
    def check(self):
        self.grid.disable(True)
        self.update_model()
        if self.solver.check_board():
            self._show_message("Congratulations! You have successfully solved the sudoku!")
        else:
            self.grid.disable(False)
            self._show_message("Try again! You can reset or make changes to your current solution.")

    def _update_board(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.board[i][j] = board[i][j]

    def _reset_board(self):
        self.grid.disable(False)
        self._hide_message()
        self._update_board(self.original_board)
        self.grid.reset()

    def exitApp(self):
        exit()   