# runtime = 25.0ms
# memory usage = 16.7MB

class Solution:
    def __init__(self):
        self.ans = set()

    def get_subset(self, nums, index = 0, temp = []):
        if len(temp) <= len(nums):
            self.ans.add(tuple(temp.copy()))
        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.get_subset(nums, i+1, temp)
            temp.pop(-1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.get_subset(sorted(nums))
        return self.ans