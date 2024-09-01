# runtime = 536.0ms
# memory usage = 11.7MB

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        sub_len = 1
        while(sub_len <= len(s)):
            s_i = 0
            while(s_i + sub_len <= len(s)):
                sub_str = s[s_i : s_i + sub_len]
                if sub_str == sub_str[::-1]:
                    c += 1
                s_i += 1
            sub_len += 1
        return c
        