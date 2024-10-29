class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        stepCount = {(i, j):-float('inf') for i in range(len(grid)) \
         for j in range(len(grid[0]))}
        ret = 0

        def maximizeStepCount(pos: List[int]) -> None:
            nonlocal ret
            row, col = pos
            next_positions = [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]

            for next_pos in next_positions:
                if next_pos in stepCount:
                    if grid[row][col] < grid[next_pos[0]][next_pos[1]]:
                        if stepCount[pos] + 1 > stepCount[next_pos]:
                            stepCount[next_pos] = stepCount[pos] + 1
                            ret = max(ret, stepCount[next_pos])
                            maximizeStepCount(next_pos)

        for i in range(len(grid)):
            stepCount[(i, 0)] = 0
            maximizeStepCount((i, 0))
        return ret