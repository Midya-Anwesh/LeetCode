# runtime = 137.0ms
# memory usage = 18.0MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        s = defaultdict(lambda : 0)
        for ele in nums:
            s[ele] += 1
        ret = nums[0]
        for ele in s:
            if s[ele] > s[ret]:
                ret = ele
        return ret