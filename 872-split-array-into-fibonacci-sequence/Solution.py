# runtime = 8574.0ms
# memory usage = 16.6MB

import re

class Solution:
    def valid(self, arr):
        for i in range(2, len(arr)):
            if arr[i] != arr[i-1]+arr[i-2] or arr[i] >= 2147483648:
                return False
        return True

    def gen(self, num: str, index: int = 0, temp: list[str] = []):
        if index >= len(num) and len(temp) >= 3:
            self.ret = temp.copy()
            self.solved = True
            return

        for i in range(index, len(num)+1):
            if self.solved:
                return
            s = num[index:i]
            if re.fullmatch(r"(?:0|(?:[1-9][0-9]*))", s):
                if len(temp) <= 1:
                    temp.append(int(s))
                    self.gen(num, i)
                    temp.pop(-1)
                else:
                    temp.append(int(s))
                    if temp[-1] < 2147483648 and self.valid(temp):
                        self.gen(num, i)
                    temp.pop(-1)
            elif s != "" and ((index > 0 and s == "0") or int(s) >= 2147483648):
                return

    def splitIntoFibonacci(self, num: str) -> list[int]:
        self.ret, self.solved = [], False
        self.gen(num)
        return self.ret