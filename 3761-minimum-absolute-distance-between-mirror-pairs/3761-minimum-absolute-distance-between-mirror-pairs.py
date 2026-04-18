class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        indexOf = dict()
        minDis = float('inf')
        
        for idx, num in enumerate(nums):
            # Calculate the difference of current number with it's mirror number
            minDis = min( minDis, abs(idx - indexOf.get(num, float('inf'))) )

            # Reverse the current num
            rev = 0
            while num > 0:
                rev = (rev * 10) + (num % 10)
                num //= 10

            # Update the index map
            indexOf[rev] = idx
        
        # Now return minimum distance
        if minDis >= float('inf'):
            return -1
        return minDis