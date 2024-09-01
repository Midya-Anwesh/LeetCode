# runtime = 1048.0ms
# memory usage = 16.3MB

class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, n: int, index: int = 1, seen: set = set()) -> int:
        if index > n:
            self.count += 1
            return
        
        for i in range(n):
            if (not (i+1) in seen) and (not((i+1)%index) or not(index%(i+1))):
                seen.add(i+1)
                self.countArrangement(n, index+1, seen)
                seen.discard(i+1)

        return self.count