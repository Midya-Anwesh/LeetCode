# runtime = 30.0ms
# memory usage = 16.4MB

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        return [(i + extraCandies) >= max_val for i in candies]      