from heapq import heappush, heappop
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda event: int(event[1]))
        offlineUsers = []
        online = [1 for _ in range(numberOfUsers)]
        mentions = [0 for _ in range(numberOfUsers)]

        for (msgType, time, usrIds) in events:

            while len(offlineUsers) and offlineUsers[0][0] + 60 <= int(time):
                _, uId = heappop(offlineUsers)
                online[uId] = 1

            if msgType == "MESSAGE":
                if usrIds in ("HERE", "ALL"):
                    for user in range(numberOfUsers):
                        if usrIds == "HERE" and online[user]:
                            mentions[user] += 1
                        elif usrIds == "ALL":
                            mentions[user] += 1
                else:
                    userIds = list( map(lambda uId: int(uId[2:]), usrIds.split(' ')) )
                    for uId in userIds:
                        mentions[uId] += 1

            if msgType == "OFFLINE":
                uId = int(usrIds)
                if online[uId]:
                    online[uId] = 0
                    heappush(offlineUsers, (int(time), uId))
        
        return mentions