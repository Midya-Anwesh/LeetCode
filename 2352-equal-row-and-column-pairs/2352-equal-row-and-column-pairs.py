class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans, memo = 0, dict()
        for row in range(len(grid)):
            row_key = tuple(grid[row])
            if not row_key in memo:
                memo[row_key] = [0, 0]
            memo[row_key][0] += 1

            col_key = tuple([grid[i][row] for i in range(len(grid))])
            if not col_key in memo:
                memo[col_key] = [0, 0]
            memo[col_key][1] += 1
        
        for key in memo:
            ans += (memo[key][0]*memo[key][1])
            
        return ans