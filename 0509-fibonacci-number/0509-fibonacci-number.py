from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)