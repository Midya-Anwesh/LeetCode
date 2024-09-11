from functools import reduce

class Solution:

    def xorSum(self, index, subset):

        if len(subset) and len(subset) <= len(self.nums):

            self.ret += reduce(lambda x,y=0:x^y, subset)

        for i in range(index, len(self.nums)):

            subset.append(self.nums[i])

            self.xorSum(i+1, subset)

            subset.pop(-1)

                       

    def subsetXORSum(self, nums: List[int]) -> int:

        self.nums = nums

        self.ret = 0

        self.xorSum(0, [])

                       

        return self.ret

        