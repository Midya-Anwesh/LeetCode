class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return ans.index(1)+1 if any( ans:= [word.startswith(searchWord) for word in sentence.split()]) else -1