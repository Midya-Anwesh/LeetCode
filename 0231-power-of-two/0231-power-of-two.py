class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        num = 2 ** floor(log(n, 2))
        return (num == n) or (num*2 == n)