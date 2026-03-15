import numpy as np

class Fancy:

    def __init__(self):
        self.arr = np.array([], dtype = np.int64)
        self.MOD = 1_000_000_007

    def append(self, val: int) -> None:
        self.arr = np.append(self.arr, val)
        

    def addAll(self, inc: int) -> None:
        self.arr = (self.arr + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.arr = (self.arr * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if (idx >= len(self.arr)):
            return -1
        return int(self.arr[idx])


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)