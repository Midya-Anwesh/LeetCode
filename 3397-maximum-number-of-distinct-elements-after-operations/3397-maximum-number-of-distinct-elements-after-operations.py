from typing import List, Set
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        def binary_search(l: int, r: int, usedSet: Set[int]) -> int | float:
            ret = -float('inf')
            while l <= r:
                mid = l + (r-l)//2
                if mid in usedSet:
                    l = mid+1
                else:
                    ret = mid
                    r = mid-1
            return ret
        nums.sort()
        used = set()
        distinctElements = 0

        for num in nums:
            lowestPossible = binary_search(num-k, num+k, used)
            if lowestPossible > -float('inf'):
                distinctElements += 1
                used.add(lowestPossible)
        
        return distinctElements