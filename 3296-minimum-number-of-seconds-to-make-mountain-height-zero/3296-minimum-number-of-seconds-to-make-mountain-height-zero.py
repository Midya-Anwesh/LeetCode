from math import floor

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        workerTimes.sort()
        maxTime = workerTimes[0] * ( (mountainHeight * (mountainHeight + 1)) // 2 )
        minTime = workerTimes[0]

        def canReduce(timeAllowed: int, height: int) -> bool:
            for i in range(len(workerTimes)-1, -1, -1):
                if height <= 0:
                    return True
                reduceBy = floor( ( (timeAllowed*2) / workerTimes[i] ) ** 0.5 )
                timeNeeded = workerTimes[i] * ( (reduceBy * (reduceBy + 1)) // 2 )
                if (timeNeeded > timeAllowed):
                    reduceBy -= 1
                height -= reduceBy
            return height <= 0

        minSeconds = float('inf')
        while minTime <= maxTime:
            midTime = minTime + ((maxTime - minTime) // 2)
            if (canReduce(midTime, mountainHeight)):
                minSeconds = midTime
                maxTime = midTime - 1
            else:
                minTime = midTime + 1
        
        return minSeconds