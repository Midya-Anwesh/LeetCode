class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ops = 0

        for col in range(len(grid[0])):
            for row in range(1, len(grid)):
                if grid[row][col] <= grid[row-1][col]:
                    ops += grid[row-1][col] - grid[row][col] + 1
                    grid[row][col] = grid[row-1][col] + 1
        
        return ops