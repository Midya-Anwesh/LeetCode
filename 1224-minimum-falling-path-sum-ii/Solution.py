# runtime = 7278.0ms
# memory usage = 62.3MB

from functools import lru_cache

class Solution:
    @lru_cache(maxsize = None)

    def get_min(self, pos: tuple[int]):

        i, j = pos

        if i == len(self.m)-1:

            return self.m[i][j]

        curr_min = self.m[i][j]

        min_cost = float('inf')

        row = i
        for col in range(len(self.m[0])):
            if col == j:
                continue
            min_cost = min(self.get_min((row+1, col)), min_cost)
        

        







        return curr_min + min_cost
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        self.m = grid
        min_cost = float('inf')
        for i in range(len(self.m[0])):
            min_cost = min(min_cost, self.get_min((0, i)))
        #print(self.get_min.cache_info())
        return min_cost
        