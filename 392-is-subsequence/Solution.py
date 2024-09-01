# runtime = 32.0ms
# memory usage = 16.6MB

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l_s,l_t,j = len(s),len(t),0
        for i in range(l_s):
            if j >= l_t:
                return False
            while(j < l_t and t[j]!=s[i]):
                j += 1
            if j>= l_t and t[j-1]!=s[i]:
                return False
            elif j < l_t:
                j += 1
        return True