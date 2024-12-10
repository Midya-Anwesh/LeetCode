class Solution:
    def maximumLength(self, s: str) -> int:
        st, end = 1, len(s) # min & max length of substrings which can repeat thrice

        def validate(sublen: int) -> bool:
            # set up pointers for a window of specific length
            win_st, win_end = 0, sublen-1
            # chars to track distinct characters & count to track occurence of a substring
            chars, count = dict(), dict()
            
            for i in range(win_st, win_end):
                chars[s[i]] = chars.get(s[i], 0) + 1
            
            while win_end < len(s):
                chars[s[win_end]] = chars.get(s[win_end], 0) + 1
                win_end += 1

                if len(chars) == 1:
                    substr = s[win_st:win_end]
                    count[substr] = count.get(substr, 0) + 1

                chars[s[win_st]] -= 1
                if chars[s[win_st]] == 0:
                    chars.pop(s[win_st])
                win_st += 1
            
            for substr in count:
                if count[substr] >= 3:
                    return True
            return False

        
        ans = -1
        while st <= end:
            mid = st+(end-st)//2
            if validate(mid):
                ans = max(ans, mid)
                st = mid+1
            else:
                end = mid-1
        
        return ans