class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        """
        
        In this approach we have prefix sum & suffix sum

        1. prefix[i] will store the sum of values before ith index [excluding ith index]

        2. suffix[i] will store the sum of values after ith index [including ith index]
            If we split the array at ith index, the ith element will end up in right partition
            so, suffix[i] includes element at ith index

        3. We traverse both prefix and postfix, index 1 to len(nums) to maintain the split validity
            At any index if prefix[i] >= suffix[i] that means,
            left partition has higher sum then right partition, thus we get a valid split
        
        """

        # Create prefix and suffix array
        prefix, suffix = [0] * (len(nums)+1), [0] * (len(nums)+1)

        # Filling prefix and suffix array
        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
            suffix[len(nums)-i] = suffix[len(nums)-i+1] + nums[len(nums)-i]
        
        # ans variable
        ans = 0

        for i in range(1, len(nums)):
            # Add 1 if we get a valid partition, i.e: left sum >= right sum, i.e: prefix[i] >= suffix[i]
            ans += prefix[i] >= suffix[i]
        
        # Return total number of valid splits
        return ans