class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            if num == 2:
                nums[i] = -1
            else:
                rightMost0 = 0
                while num >= 0:
                    if num&1 == 0:
                        break
                    rightMost0 += 1
                    num >>= 1
                nums[i] ^= 1 << (rightMost0 - 1)
        return nums