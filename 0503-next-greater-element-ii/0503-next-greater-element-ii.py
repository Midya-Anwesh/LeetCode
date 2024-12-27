from heapq import heapify, heappush, heappop
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ret = [-1]*len(nums)

        heap = []
        heapify(heap)

        for idx, num in enumerate(nums+nums):
            while len(heap) and num > heap[0][0]:
                minNum, retIndex = heappop(heap)
                ret[retIndex] = num
            if idx < len(nums):
                heappush(heap, (num, idx))
        
        return ret