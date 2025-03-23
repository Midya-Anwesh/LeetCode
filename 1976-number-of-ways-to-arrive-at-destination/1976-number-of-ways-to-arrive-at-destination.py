from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for source, destination, cost in roads:
            adjList[source].append([destination, cost])
            adjList[destination].append([source, cost])

        predicessor = defaultdict(list)
        def dijkstra(vertex: int) -> None:
            distance = dict()
            distance[0] = 0
            heap = [(0, 0)]
            noOfPaths = 0
            while len(heap):
                cost, vertex = heappop(heap)
                for adjNode, costToAdj in adjList[vertex]:
                    if cost + costToAdj == distance.get(adjNode, float('inf')):
                        predicessor[adjNode].append(vertex)
                    elif cost + costToAdj < distance.get(adjNode, float('inf')):
                        distance[adjNode] = cost + costToAdj
                        predicessor[adjNode].append(vertex)
                        heappush(heap, [distance[adjNode], adjNode])
        dijkstra(0)
        
        @lru_cache(maxsize=None)
        def dfs(vertex: int) -> int:
            if vertex == 0:
                return 1
            paths = 0
            for parent in predicessor[vertex]:
                paths += dfs(parent)
            return paths
        return dfs(n-1) % 1_000_000_007