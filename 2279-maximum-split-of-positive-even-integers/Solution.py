# runtime = 410.0ms
# memory usage = 45.0MB

class Solution:
    def dfs(self, n, s, temp):
        if not n:
            self.ret = temp.copy()
            return
        while (n):
            if s <= n:
                temp.append(s)
                self.dfs(n-s, s+2, temp)
                temp.pop(-1)
            if s > n or len(self.ret):
                return
            s += 2
            
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2:
            return []
        self.ret = list()
        self.dfs(finalSum, 2, [])
        return self.ret