DIRTOMOVES = {
    'N': (0, 1),
    'W': (-1, 0),
    'S': (0, -1),
    'E': (1, 0)
}

DIRS = ['N', 'W', 'S', 'E']
"""
The above arrangement gives us ->
    1. Do current idx + 1 when told to turn left 90 degree
    2. Do current idx - 1 when told to turn right 90 degree
We can get the direction we are facing by doing this
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        # Convert the obstacles list into a set for better searching
        obstacleSet = set()
        for row, col in obstacles:
            obstacleSet.add( (row, col) )

        # We would maintain a variable to track farthest distance ever convered
        maxDis = 0

        # Now we would start simulation, starting direction would be DIRS[0]
        # We would use match specified to get direction of next move if changed
        idx = 0
        row, col = 0, 0

        for command in commands:
            # If it tries to turn the robot left by 90 degree
            if command == -2:
                idx = (idx + 1) % 4 # 4 directions
            # If it tries to turn the robot right by 90 degree
            elif command == -1:
                idx = (4 + idx - 1) % 4
            # If tries to move the robot by k moves
            # Move the robot one unit at a time and maintain max distance from source accordingly
            else:
                dx, dy = DIRTOMOVES[DIRS[idx]]
                for _ in range(command):
                    nr, nc = row+dx, col+dy
                    if (nr, nc) in obstacleSet:
                        break
                    row, col = nr, nc
                    maxDis = max(maxDis, (row*row) + (col*col) )
        
        # Return max distance
        return maxDis