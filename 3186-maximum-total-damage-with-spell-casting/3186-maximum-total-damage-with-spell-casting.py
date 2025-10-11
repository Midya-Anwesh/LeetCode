from bisect import bisect_left
from functools import lru_cache

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = dict()
        for num in power:
            freq[num] = freq.get(num, 0) + 1
        power = sorted(set(power))

        @lru_cache(maxsize=None)
        def dfs(idx: int) -> int:
            if idx >= len(power):
                return 0
            maxDamage = -float('inf')
            # Check for maxDamage done by taking current element, and avoiding curr+1 and curr+2
            maxDamage = max( maxDamage, dfs(bisect_left(power, power[idx]+3)) + power[idx]*freq[power[idx]] )
            # IF curr+1 exists, check how much damage can it do, without taking current one
            if (power[idx]+1) in freq:
                maxDamage = max( maxDamage, dfs(bisect_left(power, power[idx]+1)) )
            # If curr+2 exists, checl how much damage can it do, without taking current one
            if (power[idx]+2) in freq:
                maxDamage = max( maxDamage, dfs(bisect_left(power, power[idx]+2)) )
            return maxDamage
        
        return dfs(0)
