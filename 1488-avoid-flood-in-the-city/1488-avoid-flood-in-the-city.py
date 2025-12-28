from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # nextRain will hold list of indices when there will be rain on lake i
        # nextRain[lake] = [dayN, dayN-1, ..., day1] where, dayN > dayN-1 > ... > day1
        nextRain = defaultdict(list)
        for idx, lake in enumerate(rains):
            nextRain[lake].append(idx)
        for lake in nextRain:
            nextRain[lake] = nextRain[lake][::-1][:-1]

        # To check if a lake is dry or not
        isDry = {lake: True for lake in rains}

        # we will simulate the situation with a heap, and dry a lake if it's going to rain early
        heap = []
        ret = []
        for lake in rains:
            if lake == 0:
                if len(heap):
                    _, lake = heappop(heap)
                    isDry[lake] = True
                    ret.append(lake)
                else:
                    ret.append(1)
                continue
            if isDry[lake]:
                isDry[lake] = False
                if len(nextRain[lake]):
                    heappush(heap, (nextRain[lake].pop(-1), lake))
                ret.append(-1)
            else:
                return []
        return ret
