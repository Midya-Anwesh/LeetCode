# runtime = 904.0ms
# memory usage = 28.4MB

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start, end = 1, len(nums)
        ret = curr = sum(nums[:k])
        while(start + k <= end):
            curr += nums[start+k-1]-nums[start-1]
            ret = max(ret, curr)
            start += 1
        return ret/k