class Solution:
    def countHomogenous(self, s: str) -> int:
        totalSubs, win_st, currChar = 0, 0, ''
        for i in range(len(s)):
            if s[i] != currChar:
                currChar = s[i]
                win_st = i
            totalSubs += i-win_st+1
        return totalSubs % 1_000_000_007