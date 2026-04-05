MOVES = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r, c = 0, 0
        for move in moves:
            dx, dy = MOVES[move]
            r, c = r+dx, c+dy
        return r == 0 and c == 0