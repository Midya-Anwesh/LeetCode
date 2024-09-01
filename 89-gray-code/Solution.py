# runtime = 69.0ms
# memory usage = 24.0MB

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
                res.append(res[j] | 1<<i)
        return res