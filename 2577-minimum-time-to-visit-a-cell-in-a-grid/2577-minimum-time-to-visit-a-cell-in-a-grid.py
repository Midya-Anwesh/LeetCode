from collections import deque
from heapq import heapify, heappush, heappop
ADJ_VTX = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        time = {(i, j):float('inf') for i in range(len(grid)) for j in range(len(grid[0]))}
        time[(0, 0)] = 0

        def dijkastra() -> int|None:
            heap = []
            heapify(heap)
            heappush(heap, [0, 0, 0])
            while len(heap):
                curr_time, row, col = heappop(heap)
                for dx, dy in ADJ_VTX:
                    if (row+dx, col+dy) in time:
                        time_needed = curr_time + 1
                        if curr_time < grid[row+dx][col+dy]:
                            diff = grid[row+dx][col+dy] - curr_time
                            if diff&1:
                                time_needed = grid[row+dx][col+dy]
                            else:
                                time_needed = grid[row+dx][col+dy] + 1
                        if time_needed < time[(row+dx, col+dy)]:
                            time[(row+dx, col+dy)] = time_needed
                            heappush(heap, [time_needed, row+dx, col+dy])
        dijkastra()
        return time[(len(grid)-1, len(grid[0])-1)]