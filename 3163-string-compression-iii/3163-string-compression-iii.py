class Solution:
    def compressedString(self, word: str) -> str:
        ret = ""
        count = 0
        for i in range(len(word)):
            if i > 0:
                if word[i] != word[i-1]:
                    ret += str(count)+word[i-1]
                    count = 0
                elif count == 9:
                    ret += "9"+word[i]
                    count = 0
            count += 1
        ret += str(count)+word[-1]
        return ret