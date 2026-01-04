from math import sqrt, floor

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            curr = set([1, num])
            for divisor in range(2, floor(sqrt(num))+1):
                if num % divisor == 0:
                    curr.add(divisor)
                    curr.add(num // divisor)
                    if len(curr) > 4:
                        break
            if len(curr) == 4:
                ret += sum(curr)
        return ret