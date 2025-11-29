from collections import defaultdict
from heapq import heappush, heappop
class AllOne:

    def __init__(self):
        self.buckets = defaultdict(set) # Freq -> set of strings whose count = freq
        self.strToBucket = dict() # String -> bucket number
        self.maxCounts, self.minCounts = [], []

    def inc(self, key: str) -> None:
        bucket = 1
        if key not in self.strToBucket:
            self.strToBucket[key] = 1
            self.buckets[1].add(key)
        else:
            bucket = self.strToBucket[key]
            self.buckets[bucket].remove(key)
            self.strToBucket[key] += 1
            bucket += 1
            self.buckets[bucket].add(key)

        if len(self.buckets[bucket]) == 1:
            heappush(self.maxCounts, -bucket)
            heappush(self.minCounts, bucket)

    def dec(self, key: str) -> None:
        if key not in self.strToBucket:
            return
        bucket = self.strToBucket[key]
        self.buckets[bucket].remove(key)
        if bucket >= 1:
            self.buckets[bucket-1].add(key)
            self.strToBucket[key] -= 1
        

    def getMaxKey(self) -> str:
        while len(self.maxCounts) and len(self.buckets[-self.maxCounts[0]]) <= 0:
            heappop(self.maxCounts)
        if len(self.maxCounts):
            it = iter(self.buckets[-self.maxCounts[0]])
            return next(it)
        else:
            return ""

    def getMinKey(self) -> str:
        while len(self.minCounts) and len(self.buckets[self.minCounts[0]]) <= 0:
            heappop(self.minCounts)
        if len(self.minCounts):
            it = iter(self.buckets[self.minCounts[0]])
            return next(it)
        else:
            return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()