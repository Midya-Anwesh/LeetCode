from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n, m = len(coins), len(coins[0])
        
        # dp[row][col][k] = max value from (row,col) with k neutralizations left
        dp = [[[float('-inf')] * 3 for _ in range(m)] for _ in range(n)]
        
        # Base case (bottom-right)
        for k in range(3):
            if coins[n-1][m-1] < 0 and k > 0:
                dp[n-1][m-1][k] = 0
            else:
                dp[n-1][m-1][k] = coins[n-1][m-1]
        
        # Fill DP table
        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                if row == n-1 and col == m-1:
                    continue
                
                for k in range(3):
                    best = float('-inf')
                    
                    for dx, dy in [(1,0), (0,1)]:
                        nr, nc = row + dx, col + dy
                        if nr < n and nc < m:
                            
                            # Take current cell
                            best = max(best, coins[row][col] + dp[nr][nc][k])
                            
                            # Neutralize current cell if negative
                            if coins[row][col] < 0 and k > 0:
                                best = max(best, dp[nr][nc][k-1])
                    
                    dp[row][col][k] = best
        
        return dp[0][0][2]