from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = defaultdict(list)
        minDis = float('inf')

        for idx, num in enumerate(nums):
            freq[num].append(idx)
            if len(freq[num]) >= 3:
                minDis = min(minDis, 
                abs(freq[num][0] - freq[num][1]) +  abs(freq[num][1] - freq[num][2]) + abs(freq[num][2] - freq[num][0])
                )
                freq[num] = freq[num][1:]
        
        if minDis < float('inf'):
            return minDis
        return -1