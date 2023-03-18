from Starters import *

if __name__ == "__main__":
    board = Board()
    board.readFile("../sudoku-solver-py/board.txt")

    print(board)
