from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        @lru_cache(maxsize=None)
        def costToTopFloor(currIndex: int) -> int:
            # If reached top floor then cost is 0
            if currIndex >= len(costs):
                return 0

            # If standing in a floor pay the cost of that floor
            cost = costs[currIndex]

            # Check in which way we can go to top floor with minimum cost
            # By climbing 1 floor ? or 2?
            cost += min(costToTopFloor(currIndex+1), costToTopFloor(currIndex+2))

            # Return the minimum cost
            return cost
            
        # Check cost from all possible starting state and return the minimum one
        return min(costToTopFloor(0), costToTopFloor(1))