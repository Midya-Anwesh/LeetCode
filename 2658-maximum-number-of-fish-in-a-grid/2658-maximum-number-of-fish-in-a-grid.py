ADJ_CELLS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int) -> int:
            curr = grid[row][col]
            grid[row][col] = 0
            adj = 0
            for dx, dy in ADJ_CELLS:
                nr, nc = row+dx, col+dy
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0:
                    continue
                adj += dfs(nr, nc)
            return curr + adj
        
        ret = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    ret = max(ret, dfs(row, col))
        
        return ret