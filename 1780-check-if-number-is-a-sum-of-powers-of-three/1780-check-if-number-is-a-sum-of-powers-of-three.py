class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        def isPossible(exponent: int, curr: int, target: int) -> bool:
            if curr == target:
                return True
            for i in range(exponent, 17):
                if curr + 3**i > target:
                    return False
                if isPossible(i+1, curr+3**i, target):
                    return True
            return False
        return isPossible(0, 0, n)