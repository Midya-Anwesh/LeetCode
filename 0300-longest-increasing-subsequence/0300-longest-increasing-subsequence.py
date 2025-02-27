class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def getMaxLength(index: int) -> int:
            nextMaxLength = 0
            for i in range(index+1, len(nums)):
                if nums[i] > nums[index]:
                    nextMaxLength = max(nextMaxLength, getMaxLength(i))
            return nextMaxLength + 1 # 1 for current index
        
        ret = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                ret = max(ret, getMaxLength(i))
        return ret