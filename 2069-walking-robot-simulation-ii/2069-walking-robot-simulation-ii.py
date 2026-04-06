DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # [East, North, West, South]
NAMED_DIR = ["East", "North", "West", "South"]

class Robot:

    """
    Infered ->
        1. Robot will only be able to move along the borders of the grid
        2. Robot will come to same position after moving (width * 2) + ((height - 2) * 2) units facing same direction, we will treat it as MOD
            2.1. If it is the first move and the robot at (0, 0), then after coming back to (0, 0) robot will face south instade or east
    """

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.row, self.col = 0, 0
        self.idx = 0
        self.MOD = (self.width * 2) + ((self.height - 2) * 2) # After moving self.MOD steps the robot's position will be same as current position
        self.moved = False

    def step(self, num: int) -> None:
        num = num % self.MOD
        # IF it's the first move and the robot at (0, 0), so after coming back to same cell it will face south, instade of east
        if self.row == 0 and self.col == 0 and self.moved is False:
            self.idx = 3
            self.moved = True
        
        # Do traversal of remaining steps
        traversed = 0
        while traversed < num:
            dx, dy = DIRS[self.idx]
            nr, nc = self.row+dx, self.col+dy
            # If going out of grid bounds, rotate counter clockwise and then take step
            if nr < 0 or nr >= self.height or nc < 0 or nc >= self.width:
                self.idx = (self.idx + 1) % 4
                continue
            self.row, self.col = nr, nc
            traversed += 1

    def getPos(self) -> List[int]:
        return [self.col, self.row]

    def getDir(self) -> str:
        return NAMED_DIR[self.idx]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()