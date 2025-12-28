from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        sums = []
        for i in range(len(nums1)):
            heappush(sums, (nums1[i]+nums2[0], i, 0))
        
        ret = []
        while len(ret) < k:
            _, i, j = heappop(sums)
            ret.append([nums1[i], nums2[j]])
            if j+1 < len(nums2):
                heappush(sums, (nums1[i]+nums2[j+1], i, j+1))
        
        return ret