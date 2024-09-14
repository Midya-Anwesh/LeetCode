from re import findall
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(int,(findall(r"[0-9]+", word)))))
        