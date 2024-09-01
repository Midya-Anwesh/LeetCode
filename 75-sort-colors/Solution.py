# runtime = 32.0ms
# memory usage = 16.5MB

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r,w,b, i = 0,0,0, 0
        for c in nums:
            if c == 0:
                r += 1
            elif c == 1:
                w += 1
            elif c == 2:
                b += 1
        while r:
            nums[i] = 0
            r -= 1
            i += 1
        while w:
            nums[i] = 1
            w -= 1
            i += 1
        while b:
            nums[i] = 2
            b -= 1
            i += 1