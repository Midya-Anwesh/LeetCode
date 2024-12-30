from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:

        @lru_cache(maxsize=None)
        def dfs(currStair: int) -> int:
            # If we have reached to destination, we got 1 possible way
            if currStair == n:
                return 1
            # Crossed destination invalid path
            elif currStair > n:
                return 0
            # Check all paths that we can check from current stair
            return dfs(currStair+1) + dfs(currStair+2)
        
        return dfs(0)