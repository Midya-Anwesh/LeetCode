class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        # Arr to track frequency of all characters in s
        freqArr = [0 for _ in range(26)]
        ret = ['' for _ in range(len(s))]
        # If s is odd length then the middle will remain unchanged 
        # For the smallest re-arrengement also
        # And we will count it's freqency
        if len(s)&1:
            ret[len(s)//2] = s[len(s)//2]
            freqArr[ord(s[len(s)//2]) - 97] = -1
        for char in s:
            freqArr[ord(char)-97] += 1

        # Now create the re-arrengment with smallest possible lexicographic position
        idx = 0
        mid = len(s) // 2
        for i in range(mid-1):
            while freqArr[idx] == 0:
                idx += 1
            ret[i], ret[len(s)-i-1] = chr(idx+97), chr(idx+97)
            freqArr[idx] -= 2

        while freqArr[idx] == 0:
            idx += 1
        ret[mid-1], ret[mid+(len(s)&1)] = chr(idx+97), chr(idx+97)

        return "".join(ret)