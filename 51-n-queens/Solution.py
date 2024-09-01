# runtime = 75.0ms
# memory usage = 16.7MB

class Solution:
    def __init__(self):
        self.ans = []
    
    def is_safe(self, q_no, prev_q_pos):
        for i in range(q_no):
            if (prev_q_pos[i] == prev_q_pos[q_no]) or (abs(q_no - i) == abs(prev_q_pos[i] - prev_q_pos[q_no])):
                return False
        return True
    
    def place_queen(self, n, q_no = 0, temp = []):
        if q_no >= n:
            self.ans.append(temp.copy())
            return

        for i in range(n):
            temp.append(i)
            if self.is_safe(q_no, temp):
                self.place_queen(n, q_no+1, temp)
            temp.pop(-1)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.place_queen(n)
        for valid_positions in self.ans:
            temp = []
            for position in valid_positions:
                temp.append("".join(["Q" if i == position else "." for i in range(n)]))
            yield temp