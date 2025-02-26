class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        positiveSum, negetiveSum, maxPositive, maxNegetive = max(0, nums[0]), min(0, nums[0]), nums[0], nums[0]
        for num in nums[1:]:
            positiveSum += num
            negetiveSum += num
            maxPositive = max(positiveSum, maxPositive)
            maxNegetive = min(maxNegetive, negetiveSum)
            if positiveSum <= 0:
                positiveSum = 0
            if negetiveSum >= 0:
                negetiveSum = 0
        return max(maxPositive, -maxNegetive)