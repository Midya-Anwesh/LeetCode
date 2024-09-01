# runtime = 4042.0ms
# memory usage = 16.5MB

class Solution:
    def traverse(self, i, j):
        if (i>=0 and i<len(self.grid)) and (j>=0 and j<len(self.grid[0]))\
        and self.grid[i][j] != 0:
            curr = self.grid[i][j]
            self.grid[i][j] = 0
            max_gold = 0

            moves = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for move in moves:
                temp_max = self.traverse(move[0], move[1])
                max_gold = max(temp_max, max_gold)
            self.grid[i][j] = curr
            return curr+max_gold
        
        return 0
    
    def getMaximumGold(self, grid: list[list[int]]) -> int:       
        self.grid, ret = grid, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret = max(ret, self.traverse(i, j))
        return ret