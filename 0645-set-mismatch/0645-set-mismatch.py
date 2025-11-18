class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return [nums[i], *(set(range(1, len(nums)+1)) - set(nums))]
        return []