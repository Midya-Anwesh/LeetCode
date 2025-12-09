from collections import defaultdict
from bisect import bisect_left
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        for idx, num in enumerate(nums):
            indices[num].append(idx)
        
        no_of_triplates = 0
        for idx, num in enumerate(nums):
            if num == 0:
                i = bisect_left(indices[0], idx)
                no_of_triplates += ( max(0, i * (len(indices[0])-i-1) ) )
            else:
                numsInLeft = bisect_left(indices[num*2], idx)
                numsInRight = len(indices[num*2]) - numsInLeft
                no_of_triplates += (numsInLeft * numsInRight)
        
        return no_of_triplates % 1_000_000_007