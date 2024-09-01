# runtime = 123.0ms
# memory usage = 18.3MB

class Solution:
    def explore(self, board: list[list[str]], i: int, j: int) -> None:
        board[i][j] = "S"
        moves = [(i-1, j), (i+1,j), (i, j+1), (i, j-1)]
        for move in moves:
            row, col = move
            if (row >= 0 and row < len(board)) and (col >= 0 and col < len(board[0])) and \
            board[row][col] == "O":
                self.explore(board, row, col)


    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "O" and \
                (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1):
                    self.explore(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = "O" if board[i][j] == "S" else "X"

        