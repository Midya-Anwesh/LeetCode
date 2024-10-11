class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = sorted(enumerate(times), key=lambda x:x[1][0])
        seats, ans = [], -1
        for friend, time in times:
            seated, index = False, -1
            for i in range(len(seats)):
                if seats[i][1] <= time[0]:
                    seats[i] = time
                    index = i
                    seated = True
                    break
            if not seated:
                seats.append(time)
                index = len(seats)-1

            if friend == targetFriend:
                ans = index
                break
        return ans