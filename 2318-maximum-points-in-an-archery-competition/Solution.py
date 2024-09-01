# runtime = 150.0ms
# memory usage = 47.9MB

from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def maximize(self, i: int, arrows: int) -> int:
        if self.a[i]+1 > arrows or (not arrows) or i <= 0:
            return 0
        curr_max, m = i, i
        for j in range(i-1, 0, -1):
            temp = self.maximize(j, arrows-(self.a[i]+1))
            if curr_max < m+temp:
                curr_max = m+temp
        return curr_max
    
    def find_indices(self, num: int, arrows: int) -> None:
        if not num:
            self.splitted = True
            return
        for i in range(11, 0, -1):
            if (not i in self.indices) and (num >= i) and (arrows >= self.a[i]+1):
                self.indices.add(i)
                self.find_indices(num-i, arrows-(self.a[i]+1))
                if self.splitted:
                    return
                self.indices.discard(i)

    def maximumBobPoints(self, numArrows: int, aliceArrows: list[int]) -> list[int]:
        self.a, self.indices, self.splitted = aliceArrows, set(), False
        max_score = max(self.maximize(i, numArrows) for i in range(11, 0, -1))
        self.find_indices(max_score, numArrows)
        scoreboard = [self.a[i]+1 if i in self.indices else 0 for i in range(12)]
        return [numArrows - sum(scoreboard)] + scoreboard[1:]