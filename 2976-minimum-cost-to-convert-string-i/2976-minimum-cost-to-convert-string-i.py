from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def minimumCost(self, source: str, target: str, originals: List[str], changed: List[str], costs: List[int]) -> int:
        adjList = defaultdict(list)
        for original, change, cost in zip(originals, changed, costs):
            adjList[original].append((change, cost))
        minTransitionCost = defaultdict(lambda : [float('inf') for _ in range(26)])

        def dijkstra(start: str) -> None:
            sourceIdx = ord(start)-97
            minTransitionCost[sourceIdx][sourceIdx] = 0
            heap = [(0, start)]
            while len(heap):
                currCost, currChar = heappop(heap)
                for nextChar, transitionCost in adjList[currChar]:
                    nextCharIdx = ord(nextChar)-97
                    if currCost + transitionCost < minTransitionCost[sourceIdx][nextCharIdx]:
                        minTransitionCost[sourceIdx][nextCharIdx] = currCost + transitionCost
                        heappush(heap, (currCost + transitionCost, nextChar))
        
        for i in range(97, 123):
            dijkstra(chr(i))
        
        minCost = 0
        for char1, char2 in zip(source, target):
            char1, char2 = ord(char1)-97, ord(char2)-97
            if minTransitionCost[char1][char2] >= float('inf'):
                return -1
            minCost += minTransitionCost[char1][char2]
        return minCost