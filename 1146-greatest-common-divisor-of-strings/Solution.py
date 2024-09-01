# runtime = 33.0ms
# memory usage = 16.7MB

class Solution:
    def gcd_str(self,s,k):
        l = len(s)
        for i in reversed([i for i in range(1,len(s)+1) if len(s)%i == 0]):
            sub = s[:i]
            #print(sub)
            is_valid = True
            j = 0
            while( j+i <= len(k)):
                if(k[j:j+i] != sub):
                    is_valid = False
                    break
                j += i
            if j < len(k) or l%len(sub):
                continue
            elif is_valid:
                j = 0
                v = True
                while( j+i <= len(s)):
                    if(s[j:j+i] != sub):
                        v = False
                        break
                    j += i
                if v:
                    return sub
        return ""  
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if set(str1) != set(str2):
            return ""
        if len(str1) > len(str2):
            return self.gcd_str(str2,str1)
        return self.gcd_str(str1,str2)