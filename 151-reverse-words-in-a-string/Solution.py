# runtime = 36.0ms
# memory usage = 16.6MB

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed([ch for ch in s.split(" ") if ch != ""]))