from collections import defaultdict
from bisect import bisect_left
class Solution:
    """
    To solve it, first we need to understand,
    No of triplates can be formed is (num*2 present in the left to current num) * (num*2 present in the right of current num)

    To achive this,
    We will traverse the list and store the indices to list of respective num using a hash table
    As we are traversing left to right, indices are already sorted

    So, After filling the table we can use binary search to find how many numbers are in left and right
    In case of 0 we need to substract 1 from elements present in right, as 2*0 = 0, so it resides in the same list
    """
    def specialTriplets(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        for idx, num in enumerate(nums):
            indices[num].append(idx)
        
        no_of_triplates = 0
        for idx, num in enumerate(nums):
            if num == 0:
                i = bisect_left(indices[0], idx)
                no_of_triplates += ( max(0, i * (len(indices[0])-i-1) ) )
            else:
                numsInLeft = bisect_left(indices[num*2], idx)
                numsInRight = len(indices[num*2]) - numsInLeft
                no_of_triplates += (numsInLeft * numsInRight)
        
        return no_of_triplates % 1_000_000_007