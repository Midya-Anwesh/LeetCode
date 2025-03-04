from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return log(n, 3).is_integer()