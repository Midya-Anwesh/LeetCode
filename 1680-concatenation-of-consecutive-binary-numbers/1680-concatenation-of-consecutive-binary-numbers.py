from math import log, floor
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ret = 0
        for i in range(1, n+1):
            ret = ( ret << ( floor(log(i, 2)) + 1 ) ) | i
            ret %=  1_000_000_007
        return ret 