# runtime = 34.0ms
# memory usage = 16.5MB

from math import floor, sqrt
class Solution:
    def gen(self, nums: dict(), length: int, temp: list[int] = []):
        if len(temp) == length:
            print(temp)
            self.count += 1
            return

        for num in nums:
            if nums[num] and (not len(temp) or floor(sqrt(num+temp[-1]))**2 == num+temp[-1]):
                nums[num] -= 1
                temp.append(num)
                self.gen(nums, length, temp)
                temp.pop(-1)
                nums[num] += 1

    def numSquarefulPerms(self, nums: list[int]) -> int:
        self.count, n = 0, dict()
        for num in nums:
            n[num] = n.get(num, 0) + 1
        self.gen(n, len(nums))
        return self.count