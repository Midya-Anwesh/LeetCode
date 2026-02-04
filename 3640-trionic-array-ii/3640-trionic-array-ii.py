class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        def getDec(idx: int) -> Tuple[int]:
            while idx < len(nums)-1:
                if nums[idx] < nums[idx+1]:
                    break
                elif nums[idx] == nums[idx+1]:
                    return (-1, idx)
                idx += 1
            return (0, idx)
        
        def getMaxIncSum(start: int, end: int, step: int = 1) -> int:
            maxSum, currSum = -float('inf'), nums[start]
            if step == -1:
                for i in range(start, end, step):
                    if nums[i] > nums[i+step]:
                        currSum += nums[i+step]
                        maxSum = max(maxSum, currSum)
                    else:
                        break
            else:
                for i in range(start, end):
                    if nums[i] < nums[i+1]:
                        currSum += nums[i+1]
                        maxSum = max(maxSum, currSum)
                    else:
                        break
            return maxSum
        
        p = 0
        maxSum = -float('inf')
        while p < len(nums):
            stat, q = getDec(p)
            if p == q:
                p += 1
            elif stat == -1 or q == len(nums)-1:
                p = q+1
            else:
                maxSum = max(maxSum, sum(nums[p+1:q]) + getMaxIncSum(p, 0, -1) + getMaxIncSum(q, len(nums)-1, 1) )
                p = q+1
        return maxSum