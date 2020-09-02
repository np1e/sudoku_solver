class SudokuSolver:

    def __init__(self, board=None):
        self.current_board = board


    def solve(self, board=None):
        """Computes a solution for a partially solved sudoku board.

        Args:
            board (int[][]): the sudoku board, if none is given the one provided to the class at initialization is used

        Returns:
            boolean: True, if the board could be solved, False else
        """

        if board is None:
            if self.current_board is None:
                raise ValueError
            board = self.current_board


        x, y = self._get_unassigned_cell(board) or (None, None)
        if x is None or y is None:
            return True
        
        for num in range(1,10):
            if self._is_valid(board, num, x, y):
                board[y][x] = num
                if self.solve(board):
                    return True
                board[y][x] = 0
        return False


    def _is_valid(self, board, number, x, y):
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
        if number in board[y] and board[y].index(number) != x:
            return False

        # check if number already exists in col and that is is not the number to check
        if number in [board[i][x] for i in range(9) if i != y]:
            return False

        subgrid_x = x // 3
        subgrid_y = y // 3

        # check if number exists in a 3x3 subgrid
        if number in [board[i][j] for i in range(subgrid_y * 3, subgrid_y * 3 + 3) for j in range(subgrid_x * 3, subgrid_x * 3 + 3) if i != y and j != x]:
            return False

        return True

    def _get_unassigned_cell(self, board):
        """Get an unassigned/empty cell on a given sudoku board

        Args:
            board (int[][]): the board on which to look for empty cells

        Returns:
            [type]: a tuple (x, y) with the coordinates of an empty cell, or None if there are no empty cells
        """

        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0:
                    return x, y
        return None




