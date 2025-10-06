from heapq import heappush, heappop

ADJ = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def dijkstra(row: int, col: int) -> int:
            minTime = {(i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[0]))}
            minTime[(row, col)] = grid[row][col]
            heap = [(grid[row][col], row, col)]
            while len(heap):
                currTime, r, c = heappop(heap)
                if (r == len(grid)-1) and (c == len(grid[0])-1):
                    break
                for dx, dy in ADJ:
                    nr, nc = r+dx, c+dy
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                    timeToNextNode = max(currTime, grid[nr][nc])
                    if timeToNextNode < minTime[(nr, nc)]:
                        minTime[(nr, nc)] = timeToNextNode
                        heappush(heap, (timeToNextNode, nr, nc))
            return minTime[(len(grid)-1, len(grid[0])-1)]
        return dijkstra(0, 0)