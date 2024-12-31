class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        seen = set([start])

        @lru_cache(maxsize=None)
        def dfs(i : int) -> bool:
            if not arr[i]:
                return True

            canReach = False

            if (i - arr[i] >= 0) and (not(i-arr[i] in seen)):
                seen.add(i-arr[i])
                canReach |= dfs(i-arr[i])
                seen.discard(i-arr[i])
            
            if (i + arr[i] < len(arr)) and (not(i+arr[i] in seen)):
                seen.add(i+arr[i])
                canReach |= dfs(i+arr[i])
                seen.discard(i+arr[i])
            
            return canReach
        
        return dfs(start)