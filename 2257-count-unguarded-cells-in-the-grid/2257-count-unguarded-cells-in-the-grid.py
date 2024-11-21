class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        simulated = dict()
        walls = {tuple(wall):0 for wall in walls}
        guards = {tuple(guard):0 for guard in guards}

        def simulate(row: int, col: int) -> None:

            simulated.update({(row, col):0})
            # Simulate upper cells
            for i in range(row-1, -1, -1):
                if ((i, col) in walls) or ((i, col) in guards):
                    break
                else:
                    simulated.update({(i, col):0})
            # Simulate left cells
            for j in range(col-1, -1, -1):
                if ((row, j) in walls) or ((row, j) in guards):
                    break
                else:
                    simulated.update({(row, j):0})
            # Simulate right cells
            for j in range(col+1, n):
                if ((row, j) in walls) or ((row, j) in guards):
                    break
                else:
                    simulated.update({(row, j):0})
            # Simulate down cells
            for i in range(row+1, m):
                if ((i, col) in walls) or ((i, col) in guards):
                    break
                else:
                    simulated.update({(i, col):0})
        
        for guard in guards:
            if not (guard in simulated):
                row, col = guard
                simulate(row, col)
        
        return (m*n)-(len(walls)+len(simulated))