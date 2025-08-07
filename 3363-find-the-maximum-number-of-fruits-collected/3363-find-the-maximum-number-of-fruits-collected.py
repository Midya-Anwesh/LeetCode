DIRS = {
    1 : [(1, 1), (1, 0), (0, 1)],
    2 : [(1, -1), (1, 0), (1, 1)],
    3 : [(-1, 1), (0, 1), (1, 1)]
}

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        firstChildSum = sum(fruits[i][i] for i in range(len(fruits)))
        for i in range(len(fruits)):
            fruits[i][i] = -float('inf')

        @lru_cache(maxsize=None)
        def dfs(cNo: int, row: int, col: int, stepNo: int) -> int:
            if stepNo >= len(fruits):
                return -float('inf')
            if (row == len(fruits)-1) and (col == len(fruits[0])-1):
                return fruits[len(fruits)-1][len(fruits[0])-1] if fruits[len(fruits)-1][len(fruits[0])-1] > 0 else 0

            curr = fruits[row][col]
            fruits[row][col] = -float('inf')
            nextMax = -float('inf')

            for dx, dy in DIRS[cNo]:
                nr, nc = row+dx, col+dy

                if (nr == len(fruits)-1) and (nc == len(fruits)-1):
                    nextMax = max(nextMax, dfs(cNo, nr, nc, stepNo+1))
                    continue

                if nr < 0 or nr >= len(fruits) or nc < 0 or nc >= len(fruits[0]) or fruits[nr][nc] == -float('inf'):
                    continue

                nextMax = max(nextMax, dfs(cNo, nr, nc, stepNo+1))

            fruits[row][col] = curr
            return curr + nextMax

        return firstChildSum + dfs(2, 0, len(fruits)-1, 0) + dfs(3, len(fruits)-1, 0, 0)