from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # First cache all pre-placed nums in rows, cols and sub-boxes for quick processing
        # And also, check which cells needs to be filled
        rowNums, colNums, subBoxNums = defaultdict(set), defaultdict(set), defaultdict(set)
        cells = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    rowNums[i].add(board[i][j])
                    subBoxNo = (3 * (i // 3)) + (j // 3)
                    subBoxNums[subBoxNo].add(board[i][j])
                else:
                    cells.append((i, j))

                if board[j][i] != ".":
                    colNums[i].add(board[j][i])
        
        # Functions to find if placing a number to a specific cell is safe
        def isSafe(row: int, col: int, char: str) -> bool:
            subBoxNo = (3 * (row //3)) + (col // 3)
            return (char not in rowNums[row]) and (char not in colNums[col]) and (char not in subBoxNums[subBoxNo])
        
        # Flag to mark if sudoku is solved or not
        solved = False

        # Recursive function to place digits 1-9 in vacant places to solve sudoku
        def placeDigits(idx: int) -> None:
            nonlocal solved
            if idx >= len(cells):
                solved = True
                return
            row, col = cells[idx]
            for i in range(49, 58):
                char = chr(i)
                if isSafe(row, col, char):
                    subBoxNo = (3 * (row //3)) + (col // 3)
                    board[row][col] = char
                    rowNums[row].add(char)
                    colNums[col].add(char)
                    subBoxNums[subBoxNo].add(char)
                    placeDigits(idx+1)
                    if not solved:
                        board[row][col] = "."
                        rowNums[row].discard(char)
                        colNums[col].discard(char)
                        subBoxNums[subBoxNo].discard(char)
                    else:
                        break
        
        placeDigits(0)