from math import ceil
from heapq import heappush, heappop
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Function to map cell to it's 2-d grid position as per question parameter
        # i.e: considering exam 1,  1 -> (5, 0)
        # Thanks to https://leetcode.com/problems/snakes-and-ladders/description/comments/2864672/?parent=1568241 
        def numToPos(cell):
            row = ceil(cell / len(board))
            row = abs(row - len(board))

            if (len(board) % 2 and row % 2) or (len(board) % 2 == 0 and row % 2 == 0):
                col = abs((cell % len(board)) - len(board)) if cell % len(board) else 0
            else:
                col = (cell % len(board)) - 1 if cell % len(board) else len(board) - 1

            return (row, col)

        # Function to implement dijkstra algo
        def dijkstra(start: int) -> int:
            # As we need to reach goal with lowest number of dice roll so, here we will use dice roll and the cell as the key
            # Because if we reach to two different cells then the cell which is closer to goal will be considered
            diceRolls = dict() # Map to store lowest number of dice rolls to reach a cell
            diceRolls[start] = 0
            row, col = numToPos(start) # Getting position of current cell on the grid
            # If grid[row][col] == -1 it means we can stay at that cell
            # Otherwise, there is a snake or ladder so go where it takes you
            heap = [(0, -start if board[row][col] == -1 else -board[row][col])]
            while len(heap):
                rolls, currCell = heappop(heap)
                currCell = -currCell
                # Simulate the outcome of a dice roll, (cell + 1) -> min(len(board)**2, cell+6)
                for nextCell in range(currCell+1, min(len(board)**2, currCell+6)+1):
                    if rolls + 1 < diceRolls.get(nextCell, float('inf')):
                        nr, nc = numToPos(nextCell)
                        diceRolls[nextCell] = rolls+1
                        if board[nr][nc] != -1:
                            diceRolls[board[nr][nc]] = rolls+1
                        heappush(heap, (rolls+1, -nextCell if board[nr][nc] == -1 else -board[nr][nc]))
            # Return the min roll count if exists else -1
            if diceRolls.get(len(board)**2) is None:
                return -1
            return diceRolls[len(board)**2]
        return dijkstra(1)
            