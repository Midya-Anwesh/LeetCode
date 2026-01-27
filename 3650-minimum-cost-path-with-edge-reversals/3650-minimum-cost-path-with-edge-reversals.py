from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, 2*w))
        cost = {i:float('inf') for i in range(len(edges))}
        cost[0] = 0
        heap = [(cost[0], 0)]
        while len(heap):
            currCost, vertex = heappop(heap)
            if vertex == len(edges)-1:
                return currCost
            for adjVertex, weight in adjList[vertex]:
                if currCost + weight < cost[adjVertex]:
                    cost[adjVertex] = currCost + weight
                    heappush(heap, (cost[adjVertex], adjVertex))
        return -1