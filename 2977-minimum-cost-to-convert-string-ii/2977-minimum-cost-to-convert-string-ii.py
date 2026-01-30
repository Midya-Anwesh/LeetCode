from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumCost(self, source: str, target: str, originals: List[str], changed: List[str], costs: List[int]) -> int:
        if source == target:
            return 0

        minTransitionCost = defaultdict(
            lambda: defaultdict(
                lambda: defaultdict(
                    lambda: defaultdict(
                        lambda : float('inf')
                    )
                )
            )
        )

        adjList = defaultdict(list)
        for original, change, cost in zip(originals, changed, costs):
            adjList[original].append((cost, change))

        def dijkstra(s: str) -> None:
            heap = [(0, s)]
            while len(heap):
                currCost, currStr = heappop(heap)
                for tCost, nextStr in adjList[currStr]:
                    if minTransitionCost[s[0]][s][nextStr[0]][nextStr] > currCost + tCost:
                        minTransitionCost[s[0]][s][nextStr[0]][nextStr] = currCost + tCost
                        heappush(heap, (currCost+tCost, nextStr))
        
        for original in set(originals):
            dijkstra(original)

        cost = {i: float('inf') for i in range(len(source)+1)}
        heap = [(0, 0)]
        while len(heap):
            currCost, currIdx = heappop(heap)
            if currIdx >= len(source):
                return currCost

            i = currIdx
            if source[i] == target[i]:
                if cost[i+1] > currCost:
                    cost[i+1] = currCost
                    heappush(heap, (currCost, i+1))
                    
            for substr in minTransitionCost[source[i]]:
                if source[i: i+len(substr)] == substr:
                    for substitute in minTransitionCost[source[i]][substr][target[i]]:
                        if (target[i: i+len(substitute)] == substitute) and \
                            cost[i+len(substitute)] > currCost + minTransitionCost[source[i]][substr][target[i]][substitute]:
                            cost[i+len(substitute)] = currCost + minTransitionCost[source[i]][substr][target[i]][substitute]
                            heappush(heap, (cost[i+len(substitute)], i+len(substitute)))
        
        return -1