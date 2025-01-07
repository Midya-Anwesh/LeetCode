from re import fullmatch
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [words[i] for i in range(len(words)) if any(fullmatch(fr".*{words[i]}.*", words[j]) for j in range(len(words)) if i != j)]