from re import fullmatch, match
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ans = sentence[0] == sentence[len(sentence)-1]
        for i in range(len(sentence)):
            if sentence[i] == " ":
                ans &= sentence[i-1] == sentence[i+1]
        return ans