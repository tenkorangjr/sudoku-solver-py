from Starters import *


class SudokuSolver:

    def __init__(self, board: Board) -> None:
        self.board = board

    def getBoard(self) -> Board:
        """Get the board being solved"""

        return self.board

    def findNextCell(self) -> Cell:
        """Find the next cell to be checked and modify"""

        pass

    def findNextValue(self, cell: Cell) -> int:
        """Find the next value for the cell"""

        pass

    def solve(self) -> bool:
        """Solve the board using backtracking, stacks and DFS"""

        pass
