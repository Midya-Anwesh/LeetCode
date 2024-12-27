from heapq import heapify, heappop, heappush
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = {num:i for i, num in enumerate(nums1)}

        heap, ret = [], [-1]*len(nums1)
        heapify(heap)
        for num in nums2:
            while len(heap) and heap[0] < num:
                if heap[0] in nums1:
                    ret[nums1[heappop(heap)]] = num
                else:
                    heappop(heap)
            heappush(heap, num)
        
        return ret