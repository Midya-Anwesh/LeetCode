# runtime = 124.0ms
# memory usage = 18.0MB

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = sorted(nums,key=lambda x: x==0)
        
        