class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        ret = False
        for i in range(len(s)):
            if s[i] == goal[0]:
                matched = True
                for j in range(len(goal)):
                    if s[(i+j)%len(s)] != goal[j]:
                        matched = False
                        break
                if matched:
                    ret = matched
                    break
        return ret