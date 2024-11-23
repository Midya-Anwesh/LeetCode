class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort(key=lambda pos:(pos[0], pos[1]))
        ret, last_lowest_point = 1, points[0][0]
        for i in range(1, len(points)):
            if points[i][0] - last_lowest_point > w:
                ret, last_lowest_point = ret+1, points[i][0]
        return ret