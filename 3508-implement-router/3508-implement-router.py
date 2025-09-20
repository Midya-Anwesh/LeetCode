from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
class Router:

    def __init__(self, memoryLimit: int):
        self.deq = deque() # To maintain all packet in FIFO manner
        self.memoryLimit = memoryLimit # Set the memory limit
        self.prevInserted = set() # hash table to store which packets are currently in memory
        self.destToTime = defaultdict(deque) # Maintains time-stamp queue of packets, destination wise

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # Create a packet from given information
        currPacket = (source, destination, timestamp)
        # If the packet was already inserted, don't bother
        if currPacket in self.prevInserted:
            return False
        # If the queue is in its max memory limit, remove the oldest packet
        # Also remove the reference of the packet from prevInserted and destTime
        while len(self.deq) == self.memoryLimit:
            packet = self.deq.popleft()
            self.prevInserted.remove(packet)
            self.destToTime[destination].popleft()
        # Add current/new packet and crete all references correctly
        self.deq.append(currPacket)
        self.prevInserted.add(currPacket)
        self.destToTime[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        # If there are no packet to forward return []
        if len(self.deq) == 0:
            return []
        # Get the oldest packet remove it from queue and remove all of it's references
        packet = self.deq.popleft()
        self.prevInserted.remove(packet)
        destination = packet[1]
        self.destToTime[destination].popleft()
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # Get the count using binary search
        left_idx = bisect_left(self.destToTime[destination], startTime)
        right_idx = bisect_right(self.destToTime[destination], endTime)
        return right_idx - left_idx


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)