class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        k, idx = 0, 0
        while idx < len(nums):
            if nums[idx] != nums[k]:
                nums[(k:=k+1)] = nums[idx]
            idx += 1
        return k+1