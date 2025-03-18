from heapq import heappush, heappop
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        indexOf = dict() # indexOf[1] = heap([1, 2]) means numbers at index 1 and 2 conrains 1 in position 1 in their binary representation

        maxLen, st, end = 1, 0, 0
        for i in range(len(nums)):
            pos = 0
            while nums[i]:
                # If current number has a 1 in position 'pos' in binary
                if nums[i]&1:
                    # If there are other number before it which contain 1 in position 'pos'
                    # Then adjust the starting index of current window
                    if pos in indexOf:
                        st = max(st, -indexOf[pos][0]+1)
                        heappush(indexOf[pos], -i)
                    # Otherwise just remember current index for future references
                    else:
                        indexOf[pos] = []
                        heappush(indexOf[pos], -i)
                # Now check next bit of the number   
                nums[i] >>= 1
                pos += 1
            
            # After every iteration check length of current window
            maxLen = max(maxLen, i-st+1)
        
        return maxLen