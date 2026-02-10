from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        def isBalanced(length: int) -> bool:
            isOdd = lambda num: num&1
            evenCount, oddCount, win_st = 0, 0, 0
            count = defaultdict(int)

            for i in range(min(length, len(nums))):
                if count[nums[i]] < 1:
                    if isOdd(nums[i]):
                        oddCount += 1
                    else:
                        evenCount += 1
                count[nums[i]] += 1
            if evenCount == oddCount:
                return True

            for num in nums[length:]:
                count[nums[win_st]] -= 1
                if count[nums[win_st]] == 0:
                    if isOdd(nums[win_st]):
                        oddCount -= 1
                    else:
                        evenCount -= 1
                win_st += 1

                if count[num] < 1:
                    if isOdd(num):
                        oddCount += 1
                    else:
                        evenCount += 1
                count[num] += 1

                if evenCount == oddCount:
                    return True
            return False

        for length in range(len(nums), 1, -1):
            if isBalanced(length):
                return length

        return -1