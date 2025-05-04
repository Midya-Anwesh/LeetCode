from math import comb
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs, count = dict(), 0
        for pair in dominoes:
            pair = tuple(sorted(pair))
            pairs[pair] = pairs.get(pair, 0) + 1
        for pair in pairs:
            count += comb(pairs[pair], 2)
        return count