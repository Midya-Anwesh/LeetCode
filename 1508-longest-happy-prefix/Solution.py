# runtime = 1496.0ms
# memory usage = 17.8MB

class Solution:
    def longestPrefix(self, s: str) -> str:
        l=len(s)-1
        while(l>=1):
            if s[:l]==s[-l:]:
                return s[:l]
            l -= 1
        return ""
        