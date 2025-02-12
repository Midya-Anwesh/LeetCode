class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mat = [[-float('inf'), -float('inf')] for _ in range(82)]
        maxSum = -float('inf')

        for i, num in enumerate(nums):
            digitSum = 0
            while num > 0:
                digitSum += num%10
                num //= 10
            
            if nums[i] >= mat[digitSum][0]:
                mat[digitSum][1] = mat[digitSum][0]
                mat[digitSum][0] = nums[i]

            elif nums[i] > mat[digitSum][1]:
                mat[digitSum][1] = nums[i]
            
            maxSum = max(maxSum, sum(mat[digitSum]))
        
        return maxSum if maxSum > -float('inf') else -1