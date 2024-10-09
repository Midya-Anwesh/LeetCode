class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k >= len(nums):
            return len(nums)

        ret, st, end, queue, temp = 0, 0, 0, list(), k

        if k == 0:
            for i in range(len(nums)):
                if nums[i] == 0:
                    while i < len(nums) and nums[i] == 0:
                        i += 1
                    st = i
                if i < len(nums) and nums[i] == 1:
                    ret = max(ret, i-st+1)

            return ret 
                

        while end < len(nums):
            if nums[end] == 0:
                if temp > 0:
                    queue.append(end)
                    temp -= 1
                else:
                    break
            end += 1
        
        if end >= len(nums) or k <= 0:
            return end

        ret = end

        while end < len(nums):
            if nums[end] == 0:
                st = queue.pop(0)
                queue.append(end)
            ret = max(ret, end-st)
            end += 1

        return ret