from heapq import heapify, heappush, heappop
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]
        heapify(heap)
        ans = 1
        for i in range(1, len(intervals)):
            prev_time = heappop(heap)
            if prev_time >= intervals[i][0]:
                ans += 1
                heappush(heap, prev_time)
            heappush(heap, intervals[i][1])
        return ans