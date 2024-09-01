# runtime = 148.0ms
# memory usage = 25.0MB

class Solution:
    def __init__(self):
        self.ans = set()

    def gen(self, nums, index = 0, temp = []):
        if len(temp) > 1 and len(temp) <= len(nums):
            self.ans.add(tuple(temp))

        for i in range(index, len(nums)):
            if len(temp) == 0 or nums[i] >= temp[-1]:
                temp.append(nums[i])
                self.gen(nums, i+1, temp)
                temp.pop(-1)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.gen(nums)
        return self.ans