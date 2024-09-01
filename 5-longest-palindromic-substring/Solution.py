# runtime = 4924.0ms
# memory usage = 11.8MB

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sub_len = len(s)
        while sub_len <= len(s):
            s_i = 0
            while(s_i + sub_len <= len(s)):
                sub_str = s[s_i : s_i + sub_len]
                if sub_str == sub_str[::-1]:
                    return sub_str
                s_i += 1
            sub_len -= 1               