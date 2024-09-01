# runtime = 29.0ms
# memory usage = 16.5MB

from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def tribonacci(self, n: int) -> int:
        if(n<=1):
            return max(0,n)
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)