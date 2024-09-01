# runtime = 42.0ms
# memory usage = 16.9MB

class Solution:
    def generator(self, n: int, k: int, s: str = "", f: int = 0,prev: int = 0):
        if len(s) >= n:
            if len(s) == n and not s in self.ans:
                self.ans.add(s)
                yield int(s)
            return

        if not f:
            for i in range(1,10):
                yield from self.generator(n, k, str(i), f+1, i)
            return

        if prev + k < 10:
            yield from self.generator(n, k, s+str(prev+k), f+1, prev+k)
        if prev >= k:
            yield from self.generator(n, k, s+str(prev-k), f+1, prev-k)
          
    def numsSameConsecDiff(self, n: int, k: int):
        self.ans = set()
        yield from self.generator(n, k)
