class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(300)] for _ in range(300)]
        ret = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j] = matrix[i][j]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if dp[i][j]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret += dp[i][j]
        
        return ret