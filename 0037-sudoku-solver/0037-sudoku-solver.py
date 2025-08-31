from collections import defaultdict
UNIVERSE = set([chr(i) for i in range(49, 58)])
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # First compute which digits are safe to place along a row, or column or, sub-box
        # And also, check which cells needs to be filled
        rowNums, colNums, subBoxNums = defaultdict(lambda:UNIVERSE.copy()), defaultdict(lambda:UNIVERSE.copy()), defaultdict(lambda:UNIVERSE.copy())
        cells = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    rowNums[i].discard(board[i][j])
                    subBoxNo = (3 * (i // 3)) + (j // 3)
                    subBoxNums[subBoxNo].discard(board[i][j])
                else:
                    cells.append((i, j))

                if board[j][i] != ".":
                    colNums[i].discard(board[j][i])

        solved = False

        # Recursive function to place digits 1-9 in vacant places to solve sudoku
        def placeDigits(idx: int) -> None:
            nonlocal solved
            if idx >= len(cells):
                solved = True
                return
            row, col = cells[idx]
            subBoxNo = (3 * (row //3)) + (col // 3)
            for char in rowNums[row].intersection(colNums[col]).intersection(subBoxNums[subBoxNo]):
                rowNums[row].discard(char)
                colNums[col].discard(char)
                subBoxNums[subBoxNo].discard(char)
                placeDigits(idx+1)
                if not solved:
                    rowNums[row].add(char)
                    colNums[col].add(char)
                    subBoxNums[subBoxNo].add(char)
                else:
                    board[row][col] = char
                    return

        placeDigits(0)