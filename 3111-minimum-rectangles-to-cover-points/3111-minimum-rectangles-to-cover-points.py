class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort(key=lambda pos:(pos[0], pos[1]))
        lower_ends = [points[0][0]]
        for i in range(1, len(points)):
            if points[i][0] - lower_ends[-1] > w:
                lower_ends.append(points[i][0])
        return len(lower_ends)