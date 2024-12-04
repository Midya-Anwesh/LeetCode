class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s1, s2 = 0, 0
        while s2 < len(str2) and s1 < len(str1):
            if str1[s1] == str2[s2]:
                s1 += 1
                s2 += 1
            else:
                next_alpha = chr(((ord(str1[s1])-97+1)%26)+97)
                if next_alpha == str2[s2]:
                    s1 += 1
                    s2 += 1
                else:
                    s1 += 1
        
        if s2 >= len(str2):
            return True
        return False