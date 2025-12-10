from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)
        currTime = 0
        currPos = k
        while tickets[currPos] > 0:
            if currPos == 0 and tickets[currPos] == 1:
                return currTime + 1
            ticketsToBuy = tickets.popleft()-1
            currTime += 1
            if ticketsToBuy > 0:
                tickets.append(ticketsToBuy)
            currPos = (len(tickets)+currPos-1) % len(tickets)
        return 0