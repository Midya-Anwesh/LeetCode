from random import choice
from collections import defaultdict
from heapq import heappush, heappop
class RandomizedCollection:

    def __init__(self):
        self.idxMap = defaultdict(list)
        self.nums = []

    def insert(self, val: int) -> bool:
        heappush(self.idxMap[val], -len(self.nums))
        self.nums.append(val)
        return len(self.idxMap[val]) == 1

    def remove(self, val: int) -> bool:
        if len(self.idxMap[val]) == 0:
            return False
        idx = -heappop(self.idxMap[val])
        if idx == len(self.nums)-1:
            self.nums.pop(-1)
        else:
            lastNum = self.nums[-1]
            self.nums[idx] = lastNum
            self.nums.pop(-1)
            maxIdx = heappop(self.idxMap[lastNum])
            heappush(self.idxMap[lastNum], -idx)
        return True

    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()