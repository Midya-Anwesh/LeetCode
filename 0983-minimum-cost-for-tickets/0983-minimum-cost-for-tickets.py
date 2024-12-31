from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        """

        In this solution, we are going to start from day 1
        We will consider all possible purchase options (1 day, 7 day & 30 days passes)
        We will pick the minmum one

        NOTE: We don't necessarily have to buy passes on the day which isn't in the days list

        """

        # Create a set of all days to travell
        travell_days = set(days)

        @lru_cache(maxsize=None)
        def minCost(day: int) -> int:
            # If current day is more then last day then no need for any pass 
            if day > days[-1]:
                return 0

            # If it's the last day, get a pass which costs less to get job done
            elif day == days[-1]:
                return min(costs)

            # Otherwise, check costs of buying 1 day, 7 day & 30 day passes
            # Consider the minimum one
            ans = min(
                costs[0] + minCost(day+1),
                costs[1] + minCost(day+7),
                costs[2] + minCost(day+30)
            )

            # Remember, if we are not travellig on current day,
            # Then it is not neccessary to buy a pass on this day
            # So, consider not buying a pass at current day
            # And take minimum of them
            if not (day in travell_days):
                ans = min(ans, minCost(day+1))

            # Return the minimum cost
            return ans
        
        return minCost(1)