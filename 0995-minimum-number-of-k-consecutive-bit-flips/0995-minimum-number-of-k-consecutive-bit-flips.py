class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = 0
        st, end = 0, k-1
        diffMap = dict()
        dx = 0
        while end < len(nums):
            dx ^= diffMap.get(st, 0)
            if nums[st] ^ dx == 0:
                flips += 1
                dx ^= 1
                diffMap[st] = diffMap.get(st, 0) ^ 1
                diffMap[st+k] = diffMap.get(st+k, 0) ^ 1
            nums[st] = 1
            st += 1
            end += 1
        
        while st < end:
            dx ^= diffMap.get(st, 0)
            nums[st] ^= dx
            st += 1
        
        for num in nums:
            if num == 0:
                return -1
        return flips