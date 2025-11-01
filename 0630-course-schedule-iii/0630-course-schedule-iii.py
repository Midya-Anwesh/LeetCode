from heapq import heappush, heappop
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda course : (course[1], course[0]))
        currDay = 0
        maxHeap = []
        for duration, lastDay in courses:
            if currDay + duration <= lastDay:
                currDay += duration
                heappush(maxHeap, -duration)
            else:
                if len(maxHeap) and (-1 * maxHeap[0] >= duration):
                    maxDuration = -heappop(maxHeap)
                    currDay = currDay - maxDuration + duration
                    heappush(maxHeap, -duration)
        return len(maxHeap)