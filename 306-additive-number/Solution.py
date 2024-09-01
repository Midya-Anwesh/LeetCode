# runtime = 33.0ms
# memory usage = 16.6MB

import re
class Solution:
    def __init__(self):
        self.solved = False

    def partition(self, num, index = 0, l = 0, temp = []):
        for i in range(index+1, len(num)+1):
            s = num[index:i]
            if not re.fullmatch(r"0|(?:[1-9]+[0-9]*)", s):
                continue
                
            if l < 2 and not self.solved:
                temp.append(int(s))
                self.partition(num, i, l+1, temp)
                temp.pop(-1)

            elif int(s) > sum(temp[-2:]):
                return
                
            elif l >= 2 and not self.solved:
                if int(s) == sum(temp[-2:]):
                    if i == len(num):
                        self.solved = True
                        return
                    temp.append(int(s))
                    self.partition(num, i, l+1, temp)
                    temp.pop(-1)

    def isAdditiveNumber(self, num: str) -> bool:
        self.partition(num)
        return self.solved