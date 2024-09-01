# runtime = 256.0ms
# memory usage = 25.4MB

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = dict()
        ret = []
        for ele in nums:
            if seen.get(ele,None):
                ret.append(ele)
            else:
                seen.update({ele:"seen"})
        return ret
        