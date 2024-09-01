# runtime = 53.0ms
# memory usage = 16.7MB

from functools import reduce
class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        nums, n, p = sorted(nums), -1, len(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                n = i
                
            elif nums[i] > 0:
                p = i
                break
        n = (n-1 if (n-1)%2 != 0 else n) if n else -1
        return reduce(lambda i, j=1: i*j, nums) if n==-1 and p == len(nums) else \
        reduce(lambda i, j=1: i*j, nums[:n+1]+[1]) * reduce(lambda i, j=1: i*j, nums[p:]+[1])