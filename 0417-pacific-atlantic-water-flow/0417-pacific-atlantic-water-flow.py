from collections import defaultdict
ADJ = [(1, 0), (-1, 0), (0, -1), (0, 1)]
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        waterReach = defaultdict(lambda : [False, False]) # (i, j) -> [pacific, atlantic]
        visited = set()
        def dfs(row: int, col: int, ocean: int) -> None: # 0 -> pacific, 1 -> atlantic
            visited.add((row, col))
            waterReach[(row, col)][ocean] = True
            for dx, dy in ADJ:
                nr, nc = row+dx, col+dy
                if nr < 0 or nr >= len(heights) or nc < 0 or nc >= len(heights[0]) or ((nr, nc) in visited):
                    continue
                if heights[nr][nc] >= heights[row][col]:
                    dfs(nr, nc, ocean)

        # Apply dfs for pacific
        for i in range(len(heights)):
            dfs(i, 0, 0)
        for j in range(len(heights[0])):
            dfs(0, j, 0)
        
        visited = set()

        # Apply dfs for atlantic
        for i in range(len(heights)):
            dfs(i, len(heights[0])-1, 1)
        for j in range(len(heights[0])):
            dfs(len(heights)-1, j, 1)
        
        ret = []
        for pos in waterReach:
            if all(waterReach[pos]):
                ret.append(pos)
        return ret