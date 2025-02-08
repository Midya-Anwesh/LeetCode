from heapq import heappush, heappop
from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        # Maps index to its number
        self.numAtIndex = dict()
        # Maps number to list of indices where the number occured
        self.indicesOfOccurence = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        # If specified index already occupied
        if index in self.numAtIndex:
            # We have to remove specified index from the list of indices
            # of number which is currently in the specified index
            self.indicesOfOccurence[self.numAtIndex[index]].discard(index)
        
        # Incert the specified index to list of occurence of specified number
        self.numAtIndex[index] = number
        self.indicesOfOccurence[number].add(index)
        

    def find(self, number: int) -> int:
        if len(self.indicesOfOccurence[number]):
            return self.indicesOfOccurence[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)