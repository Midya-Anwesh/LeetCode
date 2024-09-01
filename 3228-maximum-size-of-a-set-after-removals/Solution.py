# runtime = 522.0ms
# memory usage = 26.6MB

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = set(nums1)
        n2 = set(nums2)
        #print(nums1)
        if len(n1)>len(nums1)//2:
            c = abs((len(nums1)//2)-len(n1))
            for num in n1.intersection(n2):
                if c:
                    n1.discard(num)
                    c-=1
            while len(n1)>len(nums1)//2:
                n1.pop()
        #print(n1)
        if len(n2)>len(nums2)//2:
            c = abs((len(nums2)//2)-len(n2))
            for num in n2.intersection(n1):
                if c:
                    n2.discard(num)
                    c-=1
            while len(n2)>len(nums2)//2:
                n2.pop()
        #print(n2)
        return len(n1.union(n2))
        