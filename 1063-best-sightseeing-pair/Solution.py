# runtime = 344.0ms
# memory usage = 22.2MB

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_i = values[0]
        max_score = max_i+values[1]-1
        for i in range(1, len(values)):
            max_score = max(max_score, max_i+values[i]-i)
            if values[i]+i>max_i:
                max_i = values[i]+i
        return max_score
        