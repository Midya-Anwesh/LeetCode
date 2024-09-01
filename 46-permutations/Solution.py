# runtime = 32.0ms
# memory usage = 16.5MB

class Solution:
    def recursive_generator(self, nums, curr, ret, curr_len, target_len):
        if curr_len == target_len:
            ret.append(curr.copy())
            return
        for ele in nums:
            if not ele in curr:
                curr.append(ele)
                self.recursive_generator(nums, curr, ret, curr_len+1, target_len)
                curr.pop(-1)

    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.recursive_generator(nums, [], res, 0, len(nums))
        return res