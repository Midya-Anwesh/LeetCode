# runtime = 45.0ms
# memory usage = 17.3MB

class Solution:
    def is_v(self, l: str) -> bool:
        l = l.lower()
        if l in {'a','e','i','o','u'}:
            return True
        return False
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        start, end = 0, len(s)-1
        while(start < end):
            while (not self.is_v(s[start])) and (start < end):
                start += 1
            while (not self.is_v(s[end])) and (start < end):
                end -= 1
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)