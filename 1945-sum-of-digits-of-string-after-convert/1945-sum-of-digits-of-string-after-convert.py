class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sa: str = ""
        ret: int
        for char in s:
            sa += str(ord(char)-96)
        while ( (k:=k-1) >= 0):
            ret = sum(map(int, sa))
            sa = str(ret)
        return ret
        