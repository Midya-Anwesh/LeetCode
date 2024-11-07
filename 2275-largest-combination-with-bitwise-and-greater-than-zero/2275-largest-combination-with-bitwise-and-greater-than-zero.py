from functools import lru_cache
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        hashMap, maxCount = dict(), -float('inf')
        for num in candidates:
            i = 0
            while num > 0:
                hashMap[i] = hashMap.get(i, 0) + (num&1)
                maxCount = max(maxCount, hashMap[i])
                i += 1
                num >>= 1
        return maxCount
            