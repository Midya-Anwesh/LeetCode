from math import ceil
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        maxBags = len(nums) + maxOperations
        total, st, end = 0, 1, nums[0]

        def canDivide(ballCount: int) -> bool:
            ops = 0
            for num in nums:
                ops += ceil(num/ballCount) - 1
                if ops > maxOperations:
                    return False
            return True

        for num in nums:
            total += num
            end = max(end, num)

        ret = end

        while st <= end:
            mid = st + (end-st)//2
            if canDivide(mid):
                ret = min(ret, mid)
                end = mid-1
            else:
                st = mid+1

        return ret