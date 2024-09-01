# runtime = 556.0ms
# memory usage = 37.1MB

class Solution:
    def gen(self, curr, n, k, ret, curr_combi):
        if len(curr_combi) == k:
            yield curr_combi
            return
        for num in range(curr, n+1):
            curr_combi.append(num)
            yield from self.gen(num+1, n, k, ret, curr_combi)
            curr_combi.pop(-1)
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        yield from combinations([i+1 for i in range(n)], k)
        
       