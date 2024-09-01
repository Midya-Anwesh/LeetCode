# runtime = 33.0ms
# memory usage = 16.4MB

from re import *
class Solution:
    def is_valid(self, s: str) -> bool:
        p = r"0|[3-9][0-9]{,1}|2(?:[0-5]{0,2}|[0-9]|[0-4][0-9])|1[0-9]{,2}"
        return fullmatch(p, s)
    
    def place_dots(self, s: str, dot_no: int = 0, s_i: int = 0) -> list[list[int]]:
        if dot_no == 3:
            if self.is_valid(s[self.arr[2]+1:]):
                self.ret.append(self.arr.copy())
            return
        for i in range(s_i, len(s)):
            if self.is_valid(s[s_i:i+1]):
                self.arr[dot_no] = i
                self.place_dots(s, dot_no+1, i+1)
                self.arr[dot_no] = None

    def restoreIpAddresses(self, s: str) -> list[str]:
        l = len(s)
        if l < 4 or l > 12:
            return []
        self.arr, self.ret = [None, None, None], []
        self.place_dots(s)
        for partition in self.ret:
            yield s[:partition[0]+1] + "." + s[partition[0]+1:partition[1]+1] + "." + s[partition[1]+1:partition[2]+1] + "." + s[partition[2]+1:]