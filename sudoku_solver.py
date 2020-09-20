from queue import Queue

class SudokuSolver:

    class Change():
        def __init__(self, x, y, old_value, new_value):
            self.x = x
            self.y = y
            self.old_value = old_value
            self.new_value = new_value

    def __init__(self, board):
        self._board = board
        self._changes = Queue()

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, new_board):
        self._board = new_board

    def solve(self):
        """Computes a solution for a partially solved sudoku board.

        Returns:
            boolean: True, if the board could be solved, False else
        """
        x, y = self._get_unassigned_cell() or (None, None)

        if x is None or y is None:
            return True
        
        for num in range(1,10):
            if self._is_valid(num, x, y):
                self._set_number(x, y, num)
                if self.solve():
                    return True
                self._set_number(x, y, 0)
        return False

    def _set_number(self, x, y, value):
        self._changes.put(self.Change(x, y, self._board[y][x], value))
        self._board[y][x] = value

    def _is_valid(self, number, x, y):
        """Checks whether a given number is valid on a given position in a given sudoku board.

        Args:
            board (int[][]): the board against which to check
            number (int): the number to check for validity
            x (int): x index of the position to check
            y (int): y index of the position to check

        Returns:
            boolean: True, is the number is valid, False else
        """

        # check if number already exists in row and that is is not the number to check
        if number in self._board[y] and self._board[y].index(number) != x:
            return False

        # check if number already exists in col and that is is not the number to check
        if number in [self._board[i][x] for i in range(9) if i != y]:
            return False

        subgrid_x = x // 3
        subgrid_y = y // 3

        # check if number exists in a 3x3 subgrid
        if number in [self._board[i][j] for i in range(subgrid_y * 3, subgrid_y * 3 + 3) for j in range(subgrid_x * 3, subgrid_x * 3 + 3) if i != y and j != x]:
            return False

        return True

    def _get_unassigned_cell(self):
        """Get an unassigned/empty cell on a given sudoku board.

        Returns:
            tuple: a tuple (x, y) with the coordinates of an empty cell, or None if there are no empty cells
        """

        for y in range(len(self._board)):
            for x in range(len(self._board[y])):
                if self._board[y][x] == 0:
                    return x, y
        return None
    
    def _is_finished(self):
        """Checks whether the board is completely filled.

        Returns:
            boolean: True, if the board is completely filled, else False
        """
        return not self._get_unassigned_cell()

    def check_board(self):
        """Checks if the board is filled and is a correct solution according to the rules of sudoku.

        Returns:
            boolean: True, if the board is a correct solution, else False
        """

        if not self._is_finished():
            return False

        for y in range(len(self._board)):
            for x in range(len(self._board[y])):
                val = self._board[y][x]
                if not self._is_valid(val, x, y):
                    return False
        return True





