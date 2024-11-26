class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        winners = set(range(n))
        for edge in edges:
            stronger, weaker = edge
            winners.discard(weaker)
        if len(winners) == 1:
            return list(winners)[0]
        return -1