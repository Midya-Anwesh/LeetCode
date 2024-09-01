# runtime = 782.0ms
# memory usage = 43.5MB

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ret = 0
        happiness = sorted(happiness, reverse = True)
        
        for i in range(k):
            if happiness[i]-i < 0:
                break
            ret += happiness[i]-i
        return ret