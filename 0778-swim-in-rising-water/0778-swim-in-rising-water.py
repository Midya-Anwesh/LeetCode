from heapq import heapify, heappop, heappush
ADJ_CELLS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        costs = {(i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[0]))}
        costs[(0, 0)] = grid[0][0]

        def getMin(row: int, col: int) -> None:
            if row == len(grid)-1 and col == len(grid[0])-1:
                return
            heap = [(costs[(row, col)], row, col)]
            heapify(heap)
            while len(heap):
                cost, row, col = heappop(heap)
                for dx, dy in ADJ_CELLS:
                    if (row+dx, col+dy) in costs:
                        if max(cost, grid[row+dx][col+dy]) < costs[(row+dx, col+dy)]:
                            costs[(row+dx, col+dy)] = max(cost, grid[row+dx][col+dy])
                            heappush(heap, [costs[(row+dx, col+dy)], row+dx, col+dy])
        getMin(0, 0)
        return costs[(len(grid)-1, len(grid[0])-1)]