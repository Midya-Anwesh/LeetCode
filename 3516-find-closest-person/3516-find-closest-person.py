class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xDiff, yDiff = abs(x-z), abs(y-z)
        if xDiff < yDiff:
            return 1
        elif yDiff < xDiff:
            return 2
        return 0