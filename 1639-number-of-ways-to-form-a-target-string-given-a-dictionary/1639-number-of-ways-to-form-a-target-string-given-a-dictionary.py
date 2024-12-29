from collections import defaultdict
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        char_dict = defaultdict(list)
        maxDepth = -float('inf')
        freq = dict()

        for word in words:
            for idx, char in enumerate(word):
                if (idx, char) in freq:
                    freq[(idx, char)] = freq.get((idx, char), 0) + 1
                else:
                    freq[(idx, char)] = freq.get((idx, char), 0) + 1
                    char_dict[idx].append(char)
                maxDepth = max(maxDepth, idx)

        @lru_cache(maxsize=None)
        def dfs(currIndex: int, targetIndex: int) -> int:
            if targetIndex >= len(target):
                return 1
            elif currIndex > maxDepth:
                return 0
            total = 0
            total += dfs(currIndex+1, targetIndex)
            for char in char_dict[currIndex]:
                if char == target[targetIndex]:
                    total += dfs(currIndex+1, targetIndex+1) * freq[(currIndex, char)]
            return total

        ans = dfs(0, 0)
        return ans % 1_000_000_007