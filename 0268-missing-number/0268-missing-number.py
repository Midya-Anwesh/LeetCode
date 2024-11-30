class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minimum, maximum, total = min(nums), max(nums), sum(nums)
        if minimum != 0:
            return 0
        expected_sum = maximum * ((maximum+1)//2)
        diff = expected_sum - total
        if diff == 0:
            return maximum+1
        return diff