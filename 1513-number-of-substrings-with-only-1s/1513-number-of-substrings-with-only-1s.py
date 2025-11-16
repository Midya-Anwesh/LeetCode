class Solution:
    def numSub(self, s: str) -> int:
        totalSubs = 0
        win_st = 0
        for i in range(len(s)):
            if s[i] == '1':
                totalSubs += i - win_st + 1
            else:
                win_st = i + 1
        return totalSubs % 1_000_000_007