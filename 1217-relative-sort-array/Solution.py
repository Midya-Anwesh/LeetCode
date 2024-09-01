# runtime = 39.0ms
# memory usage = 16.7MB

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {arr2[i]:i for i in range(len(arr2))}
        
        return sorted(arr1, key = (lambda x:(d.get(x,inf),x)))