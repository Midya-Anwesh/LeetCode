from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        # Function to calculate cost of typing current letter, based on previous letter typed
        def getCost(prev: str | -1, curr: str) -> int:
            if prev == -1:
                return 0
            prevAscii, currAscii = ord(prev)-65, ord(curr)-65
            x1, y1 = prevAscii // 6, prevAscii % 6
            x2, y2 = currAscii // 6, currAscii % 6
            return abs(x1 - x2) + abs(y1- y2)

        @lru_cache(maxsize=None)        
        def dfs(idx: int, left: int, right: int) -> int:
            # IF no letter to type return 0
            if idx >= len(word):
                return 0
            # Return minimum of two possibilities
            return min(
                # Try typing using left finger
                dfs(idx+1, idx, right) + getCost(-1 if left == -1 else word[left], word[idx]),
                # Try typing using right finger
                dfs(idx+1, left, idx) + getCost(-1 if right == -1 else word[right], word[idx])
            )
        
        return dfs(0, -1, -1)