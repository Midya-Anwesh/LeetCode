ADJ_CELLS = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0]:
            return False
        def check(row: int, col: int, curr: int) -> bool:
            if curr == len(grid) * len(grid[0]) - 1:
                return True
            for dx, dy in ADJ_CELLS:
                nr, nc = row+dx, col+dy
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] == curr+1:
                    return check(nr, nc, curr+1)
            return False
        return check(0, 0, 0)