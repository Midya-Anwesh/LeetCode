class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        idx = events[0][0]

        longestTime = events[0][1]

        for i in range(1, len(events)):
            timediff = events[i][1] - events[i-1][1]
            if timediff > longestTime:
                longestTime = timediff
                idx = events[i][0]
            elif timediff == longestTime:
                idx = min(idx, events[i][0])
        
        return idx