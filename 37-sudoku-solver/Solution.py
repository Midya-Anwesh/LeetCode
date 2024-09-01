# runtime = 202.0ms
# memory usage = 16.4MB

class Solution:

    def __init__(self):
        self.solved = False

    def is_safe(self, char, row, coloumn, board):
        for ele in board[row]:
            if ele == char:
                return False
    
        for r in board:
            if r[coloumn] == char:
                return False

        sub_row = (row//3)*3
        sub_coloumn = (coloumn//3)*3

        for i in range(sub_row, sub_row+3):
            for j in range(sub_coloumn, sub_coloumn+3):
                if board[i][j] == char:
                    return False
                    
        return True


    def get_positions(self, board):
        ret = [(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == "."]
        return ret
    

    def solve(self, board, index):
        if index >= len(self.positions):
            self.solved = True
            return
        row, coloumn = self.positions[index]
        for i in range(1,10):
            if self.is_safe(str(i), row, coloumn, board):
                board[row][coloumn] = str(i)
                self.solve(board, index+1)
                if self.solved:
                    return
                board[row][coloumn] = "."


    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.positions = self.get_positions(board)
        self.solve(board, 0)