from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diffMap = defaultdict(set)
        badPairs = 0

        for i, num in enumerate(nums):
            badPairs += i-len(diffMap[(i-num)])
            diffMap[(i-num)].add(i)
            
        return badPairs