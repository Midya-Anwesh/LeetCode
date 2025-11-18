from bisect import bisect_left
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            nums[i] = bisect_left(sortedNums, nums[i])
        return nums