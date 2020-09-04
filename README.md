# Sudoku Solver with Backtracking

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Build Status](https://travis-ci.com/np1e/sudoku_solver.svg?branch=master)](https://travis-ci.com/np1e/sudoku_solver)


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Usage](#usage)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Run it](#run-it)




<!-- ABOUT THE PROJECT -->
## About The Project

This is a little program that solves a sudoku puzzle using the **backtracking** algorithm. For now it solves only a preconfigures partially filled sudoku board:
```
board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
```
Eventually I will add the option to provide your own board or add more preconfigures ones. There is also the option for a (very, very basic) GUI, which is built with [Tkinter](https://docs.python.org/3/library/tkinter.html).

<!-- GETTING STARTED -->
## Usage

### Prerequisites

You will need Python 3.6 to run this program. Additionally you need the Tkinter GUI library for that version of Python. Here's how to install it on Debian-based Linux distributions:
```sh
apt-get install python3-tk
```

### Installation

You really only need to clone the repository:
```sh
git clone https://github.com/np1e_/sudoku_solver.git
```
There are no additional requirements.

### Run it

```sh
python main.py
```
This will run the Sudoku Solver with a preconfigures board and output the solution to the console.

To run it with a GUI add the `--gui` flag:
```sh
python main.py --gui
```
This will open a window where you can either click "Solve" to have the board solved by the algorithm or input your own solution and click the "Check" button to check if the solution is a correct one.
