class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]*len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + (not((nums[i]&1)^(nums[i-1]&1)))
        
        ret = []
        for query in queries:
            ret.append( (prefix[query[1]]-prefix[query[0]]) < 1 )
        return ret