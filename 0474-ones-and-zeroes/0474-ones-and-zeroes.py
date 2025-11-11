from heapq import heappush, heappop
from math import sqrt

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # To find the size of largest subset od strs which have at most m 0's and n 1's
        # We first add all the str to our set, then we subtract the largest str available untill we met the condition
        # We would use heap to keep track of largest str in set
        ret = len(strs)
        zeroHeap, oneHeap = [], []
        sZero, sOne = 0, 0
        for str in strs:
            zeroCount, oneCount = 0, 0
            for char in str:
                if char == "0":
                    zeroCount += 1
                else:
                    oneCount += 1
            heappush(zeroHeap, (-zeroCount, -oneCount))
            heappush(oneHeap, (-oneCount, -zeroCount))
            sZero += zeroCount
            sOne += oneCount

        # Euclidean distance for two points
        def eucDis(x1: int, y1: int, x2: int, y2: int) -> int:
            if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
                return float('inf')
            return sqrt((x1-x2)**2 + (y1-y2)**2)
        
        while sZero > m or sOne > n:
            cand1, cand2 = (float('inf'), float('inf')), (float('inf'), float('inf'))
            if len(zeroHeap):
                cand1 = zeroHeap[0]
            if len(oneHeap):
                cand2 = oneHeap[0]
            cand1Diff = eucDis(sZero+cand1[0], sOne+cand1[0], m, n)
            cand2Diff = eucDis(sZero+cand2[1], sOne+cand2[0], m, n)
            if cand1Diff <= cand2Diff:
                heappop(zeroHeap)
                sZero += cand1[0]
                sOne += cand1[1]
            else:
                heappop(oneHeap)
                sZero += cand2[1]
                sOne += cand2[0]
            ret -= 1

        # print(sZero, sOne)
        return ret
            