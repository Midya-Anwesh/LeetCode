# runtime = 101.0ms
# memory usage = 25.0MB

from functools import lru_cache

class Solution:
    
    @lru_cache(maxsize=None)
    def get_min(self, i: int, j: int):
        if i == len(self.m)-1 and j == len(self.m[0])-1:
            return self.m[i][j]
        min_cost = float('inf')
        if i < len(self.m)-1:
            min_cost = min(min_cost, self.get_min(i+1, j))
        if j < len(self.m[0])-1:
            min_cost = min(min_cost, self.get_min(i, j+1))
        return min_cost+self.m[i][j]
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.m = grid
        return self.get_min(0, 0)
        