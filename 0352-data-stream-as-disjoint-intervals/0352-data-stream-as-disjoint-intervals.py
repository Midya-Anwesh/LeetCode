from heapq import heappush, heappop
class SummaryRanges:

    def __init__(self):
        self.rangeMap = dict()
        self.inHeap = set()
        self.heap = [] # Max heap

    def addNum(self, value: int) -> None:
        if value not in self.inHeap:
            self.inHeap.add(value)
            heappush(self.heap, -value)

    def getIntervals(self) -> List[List[int]]:
        tempHeap = []
        intervals = []
        while len(self.heap):
            num = -heappop(self.heap)
            # Add this num to temp heap for re-construction
            heappush(tempHeap, -num)
            # Now, do range adjustment
            currRange = self.rangeMap.get(num, [num, num])
            while len(self.heap) and self.heap[0] == -(currRange[0]-1): # IF it is continuation of current range
                # Merge ranges
                nextNum = -heappop(self.heap)
                nextRange = self.rangeMap.get(nextNum, [nextNum, nextNum])
                currRange = [nextRange[0], currRange[1]]
            # Otherwise, add our current range to intervals
            intervals.append(currRange)
            # Also, add the range to the following num
            self.rangeMap[num] = currRange
        # Now assign, tempHeap to self.heap
        self.heap = tempHeap
        # Return intervals in reverse
        return intervals[::-1]
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()