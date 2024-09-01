# runtime = 951.0ms
# memory usage = 21.0MB

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.list=sorted(nums, reverse = True)
        self.index = k

        
    def add(self, val: int) -> int:
        self.list.append(val)
        self.list.sort(reverse = True)
       # print(self.list)
        return self.list[self.index-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)