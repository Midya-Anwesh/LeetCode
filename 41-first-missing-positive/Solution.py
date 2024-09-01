# runtime = 264.0ms
# memory usage = 35.1MB

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        ret = 1
        m = max(nums)
        while ret <= m:
            if ret not in nums:
                return ret
            ret += 1
        return ret


        