from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row and col and 3x3 sub-boxes
        subBoxes = defaultdict(set)
        for i in range(len(board)):
            rowNums, colNums = set(), set()
            for j in range(len(board)):
                # if board[i][j] == "." or board[j][i] == ".":
                #     continue
                if board[i][j] != ".":
                    boxNo = ((len(board[0]) // 3) * (i // 3)) + (j // 3)
                    if board[i][j] in subBoxes[boxNo]:
                        print(f"pos = {i, j} boxNo = {boxNo} | {board[i][j]} repeated in sub-box {boxNo}")
                        return False
                    else:
                        subBoxes[boxNo].add(board[i][j])
                    if board[i][j] in rowNums:
                        print(f"{board[i][j]} repeated in row {i}")
                        return False
                    else:
                        rowNums.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in colNums:
                        print(f"{board[j][i]} repeated in col {i}")
                        return False
                    else:
                        colNums.add(board[j][i])
        return True