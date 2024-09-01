# runtime = 31.0ms
# memory usage = 16.5MB

class Solution:
    def count(self, n):
        if n == 1:
            return 10
        c, ret = 9, 9
        for i in range(1,n):
            ret *= c
            c -= 1
        return ret+self.count(n-1)
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        return self.count(n)
        