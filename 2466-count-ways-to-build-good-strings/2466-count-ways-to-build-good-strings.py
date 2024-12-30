from functools import lru_cache
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @lru_cache(maxsize=1_000_0)
        def dfs(idx: int) -> int:
            if idx > high:
                return 0
            if idx == high:
                return 1
            total = 0
            if idx >= low:
                total += 1
            total += dfs(idx+zero)
            total += dfs(idx+one)
            return total
        
        ans = dfs(0)
        return ans % 1_000_000_007