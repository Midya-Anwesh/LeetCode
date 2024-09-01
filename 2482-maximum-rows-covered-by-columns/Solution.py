# runtime = 58.0ms
# memory usage = 16.5MB

class Solution:

    def covered(self, matrix):

        return len(list(filter(lambda row: sum(row[i] if not i in self.col else 0 for i in \

        range(len(matrix[0]))) == 0, matrix)))

    def maximize(self, matrix, index, n):

        if not n:

            #print(self.col, self.covered(matrix))

            self.ret = max(self.ret, self.covered(matrix))

        for i in range(index, len(matrix[0])):

            if not i in self.col:

                self.col.add(i)

                self.maximize(matrix, i+1, n-1)

                self.col.discard(i)

    def maximumRows(self, matrix: list[list[int]], numSelect: int) -> int:

        self.col = set()

        self.ret = 0

        if numSelect >= len(matrix[0]):

            return len(matrix)

        self.maximize(matrix, 0, numSelect)

        return self.ret

        