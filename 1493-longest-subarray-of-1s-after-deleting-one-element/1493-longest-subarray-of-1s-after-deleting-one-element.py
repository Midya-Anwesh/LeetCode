class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ret, st, end, queue = 0, 0, 0, list()
        for i in range(len(nums)):
            if nums[i] == 0:
                end = i
                queue.append(i)
                break
            ret = max(ret, i+1)

        if ret == len(nums):
            return ret-1

        while end < len(nums):
            end += 1
            while end < len(nums) and nums[end] == 1:
                ret = max(ret, end-st)
                end += 1
            if end < len(nums) and len(queue):
                st = queue.pop(0)+1
                queue.append(end)

        return ret