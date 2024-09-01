# runtime = 1139.0ms
# memory usage = 16.8MB

from functools import reduce

class Solution:

    def count(self, nums: list[int], temp: list[int], index: int):

        if len(temp) and len(temp) <= len(nums):

            val = reduce(lambda i, j=1: i|j, temp)

            self.or_dict[val] = self.or_dict.get(val, 0)+1

            

        for i in range (index, len(nums)):

            temp.append(nums[i])

            self.count(nums, temp, i+1)

            temp.pop(-1)

    def countMaxOrSubsets(self, nums: list[int]) -> int:

      self.or_dict = dict()

      self.count(nums, [], 0)

      return self.or_dict[max(self.or_dict)]

