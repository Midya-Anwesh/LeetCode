from functools import lru_cache
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        setBits = dict()
        for num in nums:
            no_of_set_bits = 0
            temp = num
            while temp > 0:
                no_of_set_bits += temp&1
                temp >>= 1
            setBits[num] = no_of_set_bits

        asc = sorted(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if nums[j] > nums[j+1]:
                    if setBits[nums[j]] == setBits[nums[j+1]]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
        
        return nums == asc