# runtime = 74.0ms
# memory usage = 16.6MB

class Solution:
    def count_paths(self, grid:list[list[int]], i: int, j: int, square_count: int):
        self.walked.update({tuple([i,j]): 0})

        if grid[i][j] == 2 and square_count == len(self.walked):
            self.path_count += 1
            return

        moves = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for move in moves:
            row,coloumn = move[0], move[1]
            if (row >= 0 and row <= len(grid)-1) and (coloumn >= 0 and coloumn <= len(grid[0])-1) \
                and (grid[row][coloumn]%2==0) and (not move in self.walked):
                self.count_paths(grid, row, coloumn, square_count)
                del self.walked[move]
                
                
            
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        self.path_count, self.walked = 0, dict()
        row, coloumn, square_count = 0, 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row, coloumn = i, j
                if (not grid[i][j]%2) or (grid[i][j]==1):
                    square_count += 1
        self.count_paths(grid, row, coloumn, square_count)
        return self.path_count