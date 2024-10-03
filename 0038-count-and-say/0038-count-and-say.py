class Solution:
    def recurse(self, n: int, curr: int, encoding: str) -> str:
        if curr >= n:
            return encoding
        count, ch, new_encoding = 1, encoding[0], ""
        for i in range(1, len(encoding)):
            if ch == encoding[i]:
                count += 1
            else:
                new_encoding += str(count)+ch
                count, ch = 1, encoding[i]
        new_encoding += str(count)+ch
        return self.recurse(n, curr+1, new_encoding)

    def countAndSay(self, n: int) -> str:
        return self.recurse(n, 1, "1")