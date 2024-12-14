from heapq import heapify, heappush, heappop

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans, win_st, win_end = 0, 0, 0
        maxheap, minheap = [], []
        heapify(maxheap)
        heapify(minheap)

        while win_end < len(nums):
            
            while len(maxheap):
                max_num, idx = heappop(maxheap)
                if 0 <= abs(-1*max_num-nums[win_end]) <= 2:
                    heappush(maxheap, (max_num, idx))
                    break
                win_st = max(win_st, idx+1)

            while len(minheap):
                min_num, idx = heappop(minheap)
                if 0 <= abs(min_num-nums[win_end]) <= 2:
                    heappush(minheap, (min_num, idx))
                    break
                win_st = max(win_st, idx+1)

            ans += win_end-win_st+1
            heappush(maxheap, (-1*nums[win_end], win_end))
            heappush(minheap, (nums[win_end], win_end))
            win_end += 1
            
        return ans