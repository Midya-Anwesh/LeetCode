from re import fullmatch
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum([bool(fullmatch(fr"{words[i]}.*", words[j]) and fullmatch(fr".*{words[i]}", words[j])) for i in range(len(words)) for j in range(i+1, len(words))])