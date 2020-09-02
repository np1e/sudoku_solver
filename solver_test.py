from solver import SudokuSolver
import pytest
import unittest
import copy
import random

solved_board = [
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 8, 6, 3, 1, 9]]

empty_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def test_get_empty_cell_with_one_empty_cell():
    board = copy.deepcopy(solved_board)
    empty_x, empty_y = 3, 5
    board[empty_y][empty_x] = 0

    sudoku_solver = SudokuSolver()
    x, y = sudoku_solver._get_unassigned_cell(board)
    assert x == empty_x and y == empty_y

def test_get_empty_cell_no_empty_cells():
    sudoku_solver = SudokuSolver()
    x, y = sudoku_solver._get_unassigned_cell(solved_board) or (None, None)
    assert x is None

def test_is_valid_with_valid_number():
    sudoku_solver = SudokuSolver()
    x, y = 4, 7
    number = solved_board[y][x]
    board = copy.deepcopy(solved_board)
    board[y][x] = 0

    valid = sudoku_solver._is_valid(board, number, x, y)

    assert valid

def test_is_valid_with_invalid_number():
    sudoku_solver = SudokuSolver()
    x, y = 4, 7
    valid_number = solved_board[y][x]

    random_num = valid_number
    while(random_num == valid_number):
        random_num = random.randint(1, 9)
    invalid_number = random_num

    board = copy.deepcopy(solved_board)
    board[y][x] = 0

    valid = sudoku_solver._is_valid(board, invalid_number, x, y)

    assert not valid

def test_is_valid_with_solved_board():
    sudoku_solver = SudokuSolver()
    x, y = 4, 7
    number = solved_board[y][x]

    valid = sudoku_solver._is_valid(solved_board, number, x, y)

    assert valid

def test_is_valid_duplicate_in_row():
    sudoku_solver = SudokuSolver()

    x, y = 4, 0
    number = 4
    empty_board[y][7] = number

    valid = sudoku_solver._is_valid(empty_board, number, x, y)
    assert not valid

def test_is_valid_duplicate_in_column():
    sudoku_solver = SudokuSolver()

    x, y = 4, 0
    number = 4
    empty_board[1][x] = number

    valid = sudoku_solver._is_valid(empty_board, number, x, y)
    assert not valid

def test_is_valid_duplicate_in_subgrid():
    sudoku_solver = SudokuSolver()

    x,y = 0,0
    number = 4
    empty_board[y+1][x+1] = number

    valid = sudoku_solver._is_valid(empty_board, number, x, y)
    assert not valid
