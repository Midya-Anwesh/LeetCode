from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        # Function to calculate cost of typing current letter, based on previous letter typed
        def getCost(prev: int, curr: int) -> int:
            if prev == -1:
                return 0
            prevAscii, currAscii = ord(word[prev])-65, ord(word[curr])-65
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
                dfs(idx+1, idx, right) + getCost(left, idx),
                # Try typing using right finger
                dfs(idx+1, left, idx) + getCost(right, idx)
            )
        
        return dfs(0, -1, -1)