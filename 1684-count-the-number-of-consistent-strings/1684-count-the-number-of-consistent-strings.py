class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count, universe = 0, set(allowed)
        for _ in filter(lambda word:word.issubset(universe), map(set, words)):
            count += 1
        return count