from functools import lru_cache

DIRS = [(1, 0), (0, 1)] #[ Down, Right ]
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dfs(row: int, col: int) -> Tuple[int, int]:
            if (row == len(grid)-1 and col == len(grid[0])-1):
                return (grid[row][col], grid[row][col])                
            maxTillNow = -float('inf')
            minTillNow = float('inf')
            for dx, dy in DIRS:
                nr, nc = row+dx, col+dy
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                nextMax, nextMin = dfs(nr, nc)
                if grid[row][col] < 0:
                    maxTillNow = max(maxTillNow, nextMin * grid[row][col])
                    minTillNow = min(minTillNow, nextMax * grid[row][col])
                else:
                    maxTillNow = max(maxTillNow, nextMax * grid[row][col])
                    minTillNow = min(minTillNow, nextMin * grid[row][col])
            return (maxTillNow, minTillNow)
        ret = dfs(0, 0)
        if max(ret) < 0:
            return -1
        return max(ret) % 1_000_000_007

