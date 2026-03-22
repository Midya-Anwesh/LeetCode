class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            for j in range(k+i):
                grid[x][y+j], grid[x+k-i-1][y+j] = grid[x+k-i-1][y+j], grid[x][y+j]
            x, k = x+1, k-1
        return grid