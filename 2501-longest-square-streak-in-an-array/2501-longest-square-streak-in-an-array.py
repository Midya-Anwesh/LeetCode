class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = {num:1 for num in nums}
        ret = -1

        def dfs(num: int) -> int:
            if not num in nums:
                return 0
            if not nums[num]:
                return 0
            nums[num] = 0
            left_len = dfs(num**(1/2))
            right_len = dfs(num*num)
            return left_len + right_len + 1

        for num in nums:
            if nums[num]:
                len_of_longest = -1 if (l:=dfs(num)) <= 1 else l
                ret = max(ret, len_of_longest)

        return ret