class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = dict()
        zerosRow = dict()
        onesCol = dict()
        zerosCol = dict()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zerosRow[i] = zerosRow.get(i, 0) + 1
                    zerosCol[j] = zerosCol.get(j, 0) + 1
                elif grid[i][j] == 1:
                    onesRow[i] = onesRow.get(i, 0) + 1
                    onesCol[j] = onesCol.get(j, 0) + 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = onesRow.get(i, 0) + onesCol.get(j, 0) - zerosRow.get(i, 0) - zerosCol.get(j, 0)
        
        return grid