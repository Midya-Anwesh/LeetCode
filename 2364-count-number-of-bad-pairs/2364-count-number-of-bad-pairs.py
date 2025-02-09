from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diffMap = defaultdict(set)
        badPairs = 0

        for i, num in enumerate(nums):
            diffMap[(i-num)].add(i)
            badPairs += len(diffMap) - 1
        
        return badPairs