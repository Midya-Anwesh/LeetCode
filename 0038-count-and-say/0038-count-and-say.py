class Solution:
    def countAndSay(self, n: int) -> str:
        old, new = "1", ""
        for i in range(n-1):
            count, ch = 1, old[0]
            for i in range(1, len(old)):
                if ch == old[i]:
                    count += 1
                else:
                    new += str(count)+ch
                    count, ch = 1, old[i]
            new += str(count)+ch
            old, new = new, ""
        return old