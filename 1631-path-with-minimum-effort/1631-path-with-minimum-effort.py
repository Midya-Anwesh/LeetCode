from heapq import heapify, heappop, heappush
ADJ_CELLS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        efforts = {(i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[0]))}
        efforts[(0, 0)] = 0

        def getMin(row: int, col: int) -> None:
            if row == len(grid)-1 and col == len(grid[0])-1:
                return
            heap = [(efforts[(row, col)], row, col)]
            heapify(heap)
            while len(heap):
                cost, row, col = heappop(heap)
                for dx, dy in ADJ_CELLS:
                    if (row+dx, col+dy) in efforts:
                        if (effort := max(cost, abs(grid[row][col] - grid[row+dx][col+dy]))) < efforts[(row+dx, col+dy)]:
                            efforts[(row+dx, col+dy)] = effort
                            heappush(heap, [effort, row+dx, col+dy])
        getMin(0, 0)
        return efforts[(len(grid)-1, len(grid[0])-1)]