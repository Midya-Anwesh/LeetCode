class Solution:
    def jump(self, nums: List[int]) -> int:


        """
        
        This solution is based upon memoization
        1. If our current index is last index to reach then we return 0

        2. We check every possible path from current index (i), that are
            a. i to min(i+j, n) where j in nums[i]

        3. For every jump / recursive call, the cost is 1 [this is important] 
        
        """
        
        @lru_cache(maxsize=None)
        def dfs(i: int) -> int:
            
            # If we are at last index, we reached destination, return 0
            if i >= len(nums)-1:
                return 0
        
            # Initialize minCost variable to store min-Cost between all possible paths from current index
            minCost = float('inf')

            # Traverse all reachable indices from current index
            for j in range(1, nums[i]+1):

                # If it satifies our condition then we calculate cost of that path
                if i+j < len(nums):

                    # Store the minimum of previously visited paths and current path
                    # As for every possible jump cost is 1 so, we take:
                    # minimum of previously visited minimum and (cost of newly choosen path + 1)
                    minCost = min(minCost, 1 + dfs(i+j))

            # Return the minimum value
            return minCost

        return dfs(0)