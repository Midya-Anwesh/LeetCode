class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars = dict()
        for char in s:
            chars[char] = chars.get(char, 0) + 1

        curr_max = max(chars) # This will take O(26)

        ret = ""

        while len(chars) > 1:
            if chars[curr_max] > repeatLimit:
                ret += curr_max*repeatLimit
                chars[curr_max] -= repeatLimit
                # Find next largest for separator O(26)
                for i in range(ord(curr_max)-1, 96, -1):
                    char = chr(i)
                    if chars.get(char, 0):
                        ret += char
                        chars[char] -= 1
                        if not chars[char]:
                            chars.pop(char)
                        break
            else:
                ret += curr_max*min(chars[curr_max], repeatLimit)
                chars.pop(curr_max)
                curr_max = max(chars) # next max O(26)
        
        if len(chars) == 1:
            char = next(iter(chars))
            if ret == "" or ret[-1] != char:
                ret += char * min(chars[char], repeatLimit)
        
        return ret