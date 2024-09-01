# runtime = 30.0ms
# memory usage = 16.5MB

class Solution:
    def gen_subset(self, nums, curr_subset, all_subset, curr_len, target_len, index = 0):
        if curr_len <= target_len:
            # print(curr_subset)
            all_subset.append(curr_subset.copy())
            for i in range(index, target_len):
                curr_subset.append(nums[i])
                self.gen_subset(nums, curr_subset, all_subset, curr_len+1, target_len, i+1)
                curr_subset.pop(-1)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.gen_subset(nums, [], ret, 0, len(nums))
        return ret