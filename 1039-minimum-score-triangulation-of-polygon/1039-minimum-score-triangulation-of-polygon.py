from functools import lru_cache
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(st: int, end: int) -> int:
            if st+1 == end:
                return 0
            ans = float('inf')
            for k in range(st+1, end):
                ans = min(ans,  values[st] * values[end] * values[k] + dfs(st, k) + dfs(k, end))
            return ans
        return dfs(0, len(values)-1)