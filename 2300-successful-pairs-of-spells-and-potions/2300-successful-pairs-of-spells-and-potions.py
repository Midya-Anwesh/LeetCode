from bisect import bisect_left
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        for i in range(len(spells)):
            num = ceil(success / spells[i])
            spells[i] = len(potions) - bisect_left(potions, num)
        return spells