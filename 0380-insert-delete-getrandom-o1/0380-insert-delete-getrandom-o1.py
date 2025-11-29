from random import choice
class RandomizedSet:

    def __init__(self):
        self.idxMap = dict()
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.idxMap:
            return False
        self.nums.append(val)
        self.idxMap[val] = len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idxMap:
            return False
        idx = self.idxMap[val]
        self.idxMap.pop(val)
        if idx == len(self.nums)-1:
            self.nums.pop(-1)
        else:
            self.nums[idx] = self.nums.pop(-1)
            self.idxMap[self.nums[idx]] = idx
        return True

    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()