from heapq import heapify, heappush, heappop
ADJ_CELLS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        cost = {(i, j) : float('inf') for i in range(len(grid)) for j in range(len(grid[0]))}

        def dijkstra(row: int, col: int) -> None:
            heap = [(0, row, col)]
            cost[(row, col)] = 0

            while len(heap):
                curr_cost, r, c = heappop(heap)
                if r == len(grid) and c == len(grid[0]):
                    break
                for i in range(len(ADJ_CELLS)):
                    nr, nc = r+ADJ_CELLS[i][0], c+ADJ_CELLS[i][1]

                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                    
                    if (i+1) == grid[r][c]:
                        if cost[(nr, nc)] > curr_cost:
                            cost[(nr, nc)] = curr_cost
                            heappush(heap, (curr_cost, nr, nc))
                    else:
                        if cost[(nr, nc)] > curr_cost+1:
                            cost[(nr, nc)] = curr_cost+1
                            heappush(heap, (curr_cost+1, nr, nc))
        
        dijkstra(0, 0)
        return cost[(len(grid)-1, len(grid[0])-1)]