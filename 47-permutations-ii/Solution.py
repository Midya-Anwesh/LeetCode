# runtime = 47.0ms
# memory usage = 16.6MB

class Solution:
    def recurse_generator(self, nums: list[int], curr: list[int], ret: list[list[int]], seen: dict, curr_len: int, ret_len: int):
        if curr_len == ret_len:
            ret.append(curr.copy())
            return
        
        for ele in seen:
            if seen[ele]:
                curr.append(ele)
                seen[ele] -= 1
                self.recurse_generator(nums, curr, ret, seen, curr_len+1, ret_len)
                curr.pop(-1)
                seen[ele] += 1

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        seen, ret = dict(), []
        for ele in nums:
            seen[ele] = seen.get(ele, 0) + 1
        self.recurse_generator(nums, [], ret, seen, 0, len(nums))
        return ret