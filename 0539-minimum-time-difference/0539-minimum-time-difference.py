from functools import lru_cache
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        @lru_cache(maxsize=None)
        def to_minutes(timePoint):
            hr, mn = timePoint.split(":")
            return (int(hr)*60)+int(mn)
        timePoints = list(map(to_minutes, timePoints))
        timePoints.sort()
        mn_diff = []
        for i in range(len(timePoints)):
            diff = abs(timePoints[i] - timePoints[(i+1)%len(timePoints)])
            mn_diff.append(min(1440-diff, diff))
        return sorted(mn_diff)[0]