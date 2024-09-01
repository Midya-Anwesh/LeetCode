# runtime = 125.0ms
# memory usage = 20.7MB

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        from heapq import heapify, heappush, heappop
        heapify(intervals)
        result, l = [heappop(intervals)], len(intervals)
        for _ in range(l):
            if intervals[0][0] > result[-1][1]:
                result.append(heappop(intervals))
            else:
                result[-1][1] = max(heappop(intervals)[1], result[-1][1])
        return result