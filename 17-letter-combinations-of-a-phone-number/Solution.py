# runtime = 31.0ms
# memory usage = 16.4MB

k = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}

class Solution:
   def __init__(self):
       self.sol = []
   
   def recurse(self,s,ret=""):
       for i in range(len(s)):
           for letter in k[s[i]]:
               ret += letter
               self.recurse(s[i+1:],ret)
               self.sol.append(ret) if not len(self.sol) or len(ret)==len(self.sol[-1]) else ""
               ret = ret[:-1]
   
   def letterCombinations(self, digits: str) -> list[str]:
        self.recurse(digits,"")
        return self.sol

