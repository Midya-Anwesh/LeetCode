from functools import lru_cache
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # First, we know if a sub-sequence of sum x is common between two strings we need to delete total of
            # sum(ascii of all char of s1) + sum(ascii of all char of s2) - 2*x
            # To minimize the value of above expression we need to maximize x, which we can do by
                # LCA and instade of returting the length of longest sub-sequence, return sum of the sub-sequence

        # Function to get max value of x, or max sum of common sub-squence
        @lru_cache(maxsize=None)
        def maxSumLCA(idx1: int, idx2: int) -> int:
            if idx1 >= len(s1) or idx2 >= len(s2):
                return 0
            ret = 0
            if s1[idx1] == s2[idx2]:
                ret = max(ret, ord(s1[idx1]) + maxSumLCA(idx1+1, idx2+1))
            ret = max(ret, maxSumLCA(idx1+1, idx2), maxSumLCA(idx1, idx2+1))
            return ret

        x = maxSumLCA(0, 0) # Store max sum
        
        # Now, our formula [sum(ascii of all char of s1) + sum(ascii of all char of s2) - 2*x] will give minimum total sum to be delete
        return sum(ord(char) for char in s1) + sum(ord(char) for char in s2) - 2*x