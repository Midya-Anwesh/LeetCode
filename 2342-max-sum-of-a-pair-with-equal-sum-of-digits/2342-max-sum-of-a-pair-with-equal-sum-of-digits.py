from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        numsDigitSum = list(sum(map(int, str(num))) for num in nums)
        prevSums = defaultdict(list)
        maxSum = -float('inf')

        for i, num in enumerate(numsDigitSum):
            heappush(prevSums[num], -nums[i])
            if len(prevSums[num]) >= 2:
                m1 = heappop(prevSums[num])
                m2 = heappop(prevSums[num])
                maxSum = max(maxSum, ((-1*m1) + (-1*m2)))
                heappush(prevSums[num], m1)
                heappush(prevSums[num], m2)
        
        return maxSum if maxSum > -float('inf') else -1