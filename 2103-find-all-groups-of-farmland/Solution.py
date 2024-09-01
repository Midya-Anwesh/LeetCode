# runtime = 814.0ms
# memory usage = 31.5MB

class Solution:
    def getBottomRight(self, i: int, j: int) -> None:
        if (i >= self.ret[-1][2] and j >= self.ret[-1][3]):
            self.ret[-1][2], self.ret[-1][3] = i, j

        self.land[i][j] = 0

        if (i > 0 and self.land[i-1][j]):
            self.getBottomRight(i-1, j)

        if (i < len(self.land)-1 and self.land[i+1][j]):
            self.getBottomRight(i+1, j)

        if (j > 0 and self.land[i][j-1]):
            self.getBottomRight(i, j-1)

        if (j < len(self.land[0])-1 and self.land[i][j+1]):
            self.getBottomRight(i, j+1)

    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        self.land = land
        self.ret = []
        for i in range(len(self.land)):
            for j in range(len(self.land[0])):
                if self.land[i][j]:
                    self.ret.append([i, j, i, j])
                    self.getBottomRight(i, j)
        return self.ret