class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        memo = [-2 for _ in range(32)]
        memo[0] = -1

        max_len, mask = 0, 0

        for i, char in enumerate(s):
            match (char):
                case 'a': mask ^= 1
                case 'e': mask ^= 2
                case 'i': mask ^= 4
                case 'o': mask ^= 8
                case 'u': mask ^= 16
            prev = memo[mask]
            if prev == -2:
                memo[mask] = i
            else:
                max_len = max(max_len, i-prev)
        
        return max_len