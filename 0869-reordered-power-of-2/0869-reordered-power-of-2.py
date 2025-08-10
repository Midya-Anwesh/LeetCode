from collections import defaultdict

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        requiredDigits = defaultdict(lambda : [0 for _ in range(10)])
        num = 1
        while num <= 1_000_000_000:
            temp = num
            while temp:
                requiredDigits[num][temp%10] += 1
                temp //= 10
            num <<= 1
        numDigits = [0 for _ in range(10)]
        while n:
            numDigits[n%10] += 1
            n //= 10
        for key in requiredDigits:
            if requiredDigits[key] == numDigits:
                return True
        return False