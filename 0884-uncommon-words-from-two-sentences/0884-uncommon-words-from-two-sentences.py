class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = dict()
        for word in s1.split():
            words[word] = words.get(word, 0)+1
        for word in s2.split():
            words[word] = words.get(word, 0)+1
        yield from filter(lambda word:words[word]==1, words)