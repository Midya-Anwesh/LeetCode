from heapq import heapify, heappop, heappush
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        heapify(heap)
        for idx, c in enumerate(classes):
            delta = (c[0]+1)/(c[1]+1) - c[0]/c[1]
            heappush(heap, (-delta, idx))

        while extraStudents:
            _, idx = heappop(heap)
            classes[idx][0] += 1
            classes[idx][1] += 1
            delta = (classes[idx][0]+1)/(classes[idx][1]+1) - classes[idx][0]/classes[idx][1]
            heappush(heap, (-delta, idx))
            extraStudents -= 1

        ans = 0
        for p, t in classes:
            ans += p/t
        
        return ans/len(classes)