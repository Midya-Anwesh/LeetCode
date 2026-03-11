class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        pos, ret = 0, 0
        while n:
            ret = (((n&1)^1) << pos) | ret
            n >>= 1
            pos += 1
        return ret