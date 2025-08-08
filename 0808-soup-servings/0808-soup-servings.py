CONDITIONS = [(-100, 0), (-75, -25), (-50, -50), (-25, -75)]
class Solution:
    def soupServings(self, n: int) -> float:
        @lru_cache(maxsize=None)
        def dfs(a: int, b: int) -> float:
            if b <= 0:
                if a <= 0:
                    return 0.5
                else:
                    return 0
            elif a <= 0:
                return 1
            return sum(dfs(a+dx, b+dy) * .25 for dx, dy in CONDITIONS)
        return dfs(n, n) if n < 5000 else 1        