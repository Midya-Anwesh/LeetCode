from heapq import heapify, heappush, heappop
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        if k > len(queries):
            return [-1 for _ in queries]
        
        ret = [-1 if i < k-1 else 0 for i in range(len(queries))]
        heap = []
        heapify(heap)
        for i, queries in enumerate(queries):
            heappush(heap, -1*(abs(queries[0]) + abs(queries[1])))
            if len(heap) > k:
                heappop(heap)
            if i >= k-1:
                ret[i] = heap[0]*-1
        return ret
