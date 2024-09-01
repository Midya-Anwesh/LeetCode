# runtime = 1807.0ms
# memory usage = 16.4MB

class Solution:
    def __init__(self):
        self.found = False

    def search(self, board, word, length, index = 0, row = 0, coloumn = 0):
        if index >= length:
            self.found = True
            return
        board[row][coloumn] = "."

        if not self.found and row > 0 and board[row-1][coloumn] == word[index]:
            self.search(board, word, length, index+1, row-1, coloumn)
            board[row-1][coloumn] = word[index]

        if not self.found and row < len(board)-1 and board[row+1][coloumn] == word[index]:
            self.search(board, word, length, index+1, row+1, coloumn)
            board[row+1][coloumn] = word[index]

        if not self.found and coloumn > 0 and board[row][coloumn-1] == word[index]:
            self.search(board, word, length, index+1, row, coloumn-1)
            board[row][coloumn-1] = word[index]

        if not self.found and coloumn < len(board[0])-1 and board[row][coloumn+1] == word[index]:
            self.search(board, word, length, index+1, row, coloumn+1)
            board[row][coloumn+1] = word[index]

    def exist(self, board: list[list[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.search(board, word, len(word), 1, i, j)
                    board[i][j] = word[0]
                    # if self.found:
                    #     return self.found
        return self.found