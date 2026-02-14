from collections import deque, defaultdict

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0 for _ in range(i+1)] for i in range(query_row+1) ]
        tower[0][0] = poured

        for i in range(len(tower)):
            for j in range(len(tower[i])):
                # If current cup overflows
                if tower[i][j] <= 1.0:
                    continue
                # Track how much overflows and cap it's capacity to 1
                excess = tower[i][j] - 1.0
                tower[i][j] = 1.0
                # Simulate spilling
                if i+1 < len(tower) :
                    tower[i+1][j] += excess / 2
                    tower[i+1][j+1] += excess / 2
        
        return tower[query_row][query_glass]