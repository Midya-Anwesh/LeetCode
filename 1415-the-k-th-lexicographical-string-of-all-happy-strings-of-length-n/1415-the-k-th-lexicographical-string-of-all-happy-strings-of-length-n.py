class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happyStr, gotKthString = [], False
        
        def isHappy(s: str) -> bool:
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    return False
            return True
        
        def getString(s: str) -> None:
            nonlocal gotKthString
            if len(s) >= n:
                if isHappy(s):
                    happyStr.append(s)
                    if len(happyStr) >= k:
                        gotKthString = True
                return

                    
            for char in ('a','b','c'):
                getString(s+char)
                if gotKthString:
                    return
        
        getString("")
        return happyStr[k-1] if len(happyStr) >= k else ""
        