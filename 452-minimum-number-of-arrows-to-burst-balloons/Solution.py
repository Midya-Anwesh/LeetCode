# runtime = 995.0ms
# memory usage = 62.8MB

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key=lambda ele:ele[1])
        
        l,index,count = len(points),0,1
        for i in range(1,l):
            if points[index][1]>=points[i][0] and points[index][1]<=points[i][1]:
                continue
            else:

                count += 1
                index = i
        return count








                    




