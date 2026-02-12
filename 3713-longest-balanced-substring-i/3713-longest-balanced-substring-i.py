class Solution:
    def longestBalanced(self, s: str) -> int:
        def isBalanced(length: int) -> bool:
            win_st = 0
            count = dict()
            for i in range(min(length, len(s))):
                count[s[i]] = count.get(s[i], 0) + 1
            if len(set(count.values())) == 1:
                return True
            
            for i in range(length, len(s)):
                count[s[win_st]] -= 1
                if count[s[win_st]] == 0:
                    count.pop(s[win_st])
                win_st += 1

                count[s[i]] = count.get(s[i], 0) + 1
                if len(set(count.values())) == 1:
                    return True

            return False
        
        for length in range(len(s), 0, -1):
            if isBalanced(length):
                return length
        return 0