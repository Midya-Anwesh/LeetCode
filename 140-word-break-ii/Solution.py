# runtime = 30.0ms
# memory usage = 16.4MB

class Solution:
    def __init__(self):
        self.ret = []
        self.temp = []


    def gen(self, s, wordDict, si=0):
        if si >= len(s):
            self.ret.append(" ".join(self.temp))
            return
        for i in range(si, len(s)):
            s1 = s[si:i+1]
            if s1 in wordDict:
                self.temp.append(s1)
                self.gen(s, wordDict, i+1)
                self.temp.pop(-1)

                
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = {key:0 for key in wordDict}
        self.gen(s, wordDict)

        return self.ret

