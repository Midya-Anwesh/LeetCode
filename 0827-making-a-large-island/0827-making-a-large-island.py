from typing import List, Tuple

ADJ = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        parentOf, sizeOf, seen = dict(), dict(), set()
        def dfs(row: int, col: int, parent: Tuple[int]) -> int:
            seen.add((row, col))
            parentOf[(row, col)] = parent
            currSize = 1
            for dx, dy in ADJ:
                nr, nc = row+dx, col+dy
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0 or ((nr, nc) in seen):
                    continue
                currSize += dfs(nr, nc, parent)
            sizeOf[(row, col)] = currSize
            return currSize
        
        maxSizeIsland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and ((i, j) not in seen):
                    currSize = dfs(i, j, (i, j))
                    maxSizeIsland = max(maxSizeIsland, currSize)
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    continue
                parents = set()
                for dx, dy in ADJ:
                    nr, nc = i+dx, j+dy
                    parents.add( parentOf.get((nr, nc), None) )
                mergedSize = sum(sizeOf.get(parent, 0) for parent in parents) + 1
                maxSizeIsland = max(maxSizeIsland, mergedSize)
        
        return maxSizeIsland