class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        max_arr = sorted(nums, reverse=True)
        low, high, ans = 0, 0, []
        win_or_val = 0
        while low < len(nums):
            if nums[low] == max_arr[0]:
                ans.append(1)
                low += 1
                high = low
                max_arr.pop(0)
            elif win_or_val == max_arr[0]:
                ans.append(high-low)
                low += 1
            else:
                win_or_val |= nums[high]
                high += 1
        return ans
        