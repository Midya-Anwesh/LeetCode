# runtime = 255.0ms
# memory usage = 26.4MB

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.pos = {grid[i][j]:(i, j) for i in range(len(grid)) for j in range(len(grid[0]))}

    @functools.lru_cache(maxsize = None)
    def is_valid(self, i: int, j: int) -> bool:
        return i >= 0 and i < len(self.grid) and j >= 0 and j < len(self.grid[0])

    def adjacentSum(self, value: int) -> int:
        i, j = self.pos[value]
        adj_cells = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        return sum(map(lambda pos:self.grid[pos[0]][pos[1]], filter(lambda pos:self.is_valid(pos[0], pos[1]), adj_cells) ))

    def diagonalSum(self, value: int) -> int:
        i, j = self.pos[value]
        diagonal_cells = [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
        return sum(map(lambda pos:self.grid[pos[0]][pos[1]], filter(lambda pos:self.is_valid(pos[0], pos[1]), diagonal_cells) ))


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)