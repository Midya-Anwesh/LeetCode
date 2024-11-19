class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ret = 0
        win_st, win_end = 0, k-1
        win_num_count = dict()

        curr = 0
        for i in range(k):
            win_num_count[nums[i]] = win_num_count.get(nums[i], 0) + 1
            curr += nums[i]
        if len(win_num_count) == k:
            ret = max(ret, curr)

        while win_end < len(nums)-1:
            win_num_count[nums[win_st]] -= 1
            if not win_num_count[nums[win_st]]:
                win_num_count.pop(nums[win_st])
            win_end += 1
            win_num_count[nums[win_end]] = win_num_count.get(nums[win_end], 0) + 1
            curr = curr - nums[win_st] + nums[win_end]
            win_st += 1
            if len(win_num_count) == k:
                ret = max(ret, curr)
        
        return ret