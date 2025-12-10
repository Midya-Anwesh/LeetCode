from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        stones.append(0)
        heapify(stones)
        while len(stones) > 1:
            s1, s2 = -heappop(stones), -heappop(stones)
            if s1 != s2:
                heappush(stones, -abs(s1-s2))
        return -heappop(stones)