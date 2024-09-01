# runtime = 185.0ms
# memory usage = 32.7MB

from functools import lru_cache


class Solution:
    
    @lru_cache(maxsize = None)
    def get_min(self, pos: tuple[int]):
        i, j = pos
        if i == len(self.m)-1:
            return self.m[i][j]
        curr_min = self.m[i][j]
        min_cost = self.get_min((i+1, j))
        
        if j > 0:
            min_cost = min(min_cost, self.get_min((i+1, j-1)))
        if j < len(self.m[0])-1:
            min_cost = min(min_cost, self.get_min((i+1, j+1)))
        return curr_min + min_cost
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.m = matrix
        min_cost = float('inf')
        for i in range(len(self.m)):
            min_cost = min(min_cost, self.get_min((0, i)))
        # print(self.get_min.cache_info())
        return min_cost
        