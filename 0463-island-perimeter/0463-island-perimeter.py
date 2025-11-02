ADJ = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        If there is only one cell then it's contribute 4 to perimeter
        but for each adjecent cell with value 1 the contrinution of current cell to the overall perimeter will be decrese by 1
        and incresed by perimeter that we got from those adjecent cell with value 1
        """
        vis = set()
        def getPerimeter(row: int, col: int) -> int:
            vis.add((row, col))
            currContribution = 4
            adjContribution = 0
            for dx, dy in ADJ:
                nr, nc = row+dx, col+dy
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0:
                    continue
                elif (nr, nc in vis):
                    currContribution -= 1
                    continue
                currContribution -= 1
                adjContribution += getPerimeter(nr, nc)
            return adjContribution + currContribution
        
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and ((i, j) not in vis):
                    perimeter += getPerimeter(i, j)
        return perimeter