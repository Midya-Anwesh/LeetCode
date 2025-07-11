class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        freeRooms, bookedRooms = [(i, 0) for i in range(n)], []
        meetingCount = defaultdict(int)
        for start, end in meetings:
            while len(bookedRooms) and (start >= bookedRooms[0][0]):
                prevEnd, roomNo = heappop(bookedRooms)
                heappush(freeRooms, (roomNo, prevEnd))
            roomNo, prevEnd = None, None
            if len(freeRooms):
                roomNo, prevEnd = heappop(freeRooms)
            else:
                prevEnd, roomNo = heappop(bookedRooms)
            nextEnd = max(prevEnd, start) + (end - start)
            heappush(bookedRooms, (nextEnd, roomNo))
            meetingCount[roomNo] += 1
        return max(meetingCount, key = lambda roomNo : meetingCount[roomNo])