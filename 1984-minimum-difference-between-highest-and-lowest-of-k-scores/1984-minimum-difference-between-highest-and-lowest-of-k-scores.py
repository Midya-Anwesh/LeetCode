class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = float('inf')
        for i in range(len(nums)-k+1):
            ret = min(ret, nums[i+k-1]-nums[i])
        return ret