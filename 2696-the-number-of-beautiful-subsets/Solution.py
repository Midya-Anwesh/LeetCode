# runtime = 3103.0ms
# memory usage = 16.7MB

class Solution:
    def is_valid(self, arr: list[int], k: int, num: int):
        if (((num - k) in arr) or ((num + k) in arr)):
                return False
        return True

    def count_valid_sets(self, nums: list[int], k: int, index: int = 0, temp: list[int] = list()):
        if len(temp):
            self.count += 1

        for i in range(index, len(nums)):
            if self.is_valid(temp, k, nums[i]):
                temp.append(nums[i])
                self.count_valid_sets(nums, k, i+1, temp)
                temp.pop(-1)

    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        self.count = 0
        self.mem = set()
        self.count_valid_sets(nums, k, 0, list())
        return self.count

        