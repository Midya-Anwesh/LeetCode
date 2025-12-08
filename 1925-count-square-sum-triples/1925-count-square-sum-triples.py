from math import sqrt
class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                kSquare = i**2 + j**2
                k = floor(sqrt(kSquare))
                if k == sqrt(kSquare) and k <= n:
                    res += 1
        return res