class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        k = 2**maximumBit-1
        for i in range(1, len(nums)):
            nums[i] = nums[i-1]^nums[i]
        return [nums[i]^k for i in range(len(nums)-1, -1, -1)]