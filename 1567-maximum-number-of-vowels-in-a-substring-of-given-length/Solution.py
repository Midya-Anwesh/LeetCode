# runtime = 117.0ms
# memory usage = 17.1MB

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ret,start,end = 0,1,len(s)
        v = {"a","e","i","o","u"}
        for i in range(k):
            if s[i] in v:
                ret += 1
        curr = ret
        while start+k <= end:
            if s[start-1] in v:
                curr -= 1
            if s[start+k-1] in v:
                curr += 1
            ret = max(ret,curr)
            start += 1
        return ret