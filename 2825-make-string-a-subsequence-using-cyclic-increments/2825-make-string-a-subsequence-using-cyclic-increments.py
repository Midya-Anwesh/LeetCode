class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s1, s2 = dict(), dict()
        for char in str1:
            s1[char] = s1.get(char, 0)+1
        for char in str2:
            s2[char] = s2.get(char, 0)+1

        for char in s2:
            while s2[char]:
                if s1.get(char, 0) > 0:
                    next_alpha = chr(((ord(char)-96)%26)+97)
                    prev_alpha = chr((((ord(char)-97)+25)%26)+97)
                    if s2.get(next_alpha, 0):
                        if s1[char]+s1.get(next_alpha, 0) < s2[next_alpha]:
                            return False
                        elif s1[char]+s1.get(next_alpha, 0) == s2[next_alpha]:
                            if s1.get(prev_alpha, 0):
                                s1[prev_alpha] -= 1
                                # s2[char] -= 1
                            else:
                                return False
                        else:
                            s1[char] -= 1
                            # s2[char] -= 1
                    else:
                        s1[char] -= 1

                else:
                    prev_alpha = chr((((ord(char)-97)+25)%26)+97)
                    if s1.get(prev_alpha, 0):
                        s1[prev_alpha] -= 1
                    else:
                        return False
                
                s2[char] -= 1

        return True