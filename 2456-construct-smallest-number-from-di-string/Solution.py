# runtime = 35.0ms
# memory usage = 16.4MB

class Solution:
    def gen(self, s, index, temp):
        if index > len(s):
            # self.solved = True
            self.ret = "".join(str(num) for num in temp)
            # print(self.ret)
            return
        if not index:
            for i in range(1, 10):
                temp.append(i)
                self.gen(s, index+1, temp)
                temp.pop(-1)
                
                if not self.ret is None:
                    return
        else:
            for i in range(1, 10):
                if s[index-1]=="I" and i > temp[-1] and (not i in temp):
                    temp.append(i)
                    self.gen(s, index+1, temp)
                    temp.pop(-1)
                elif s[index-1]=="D" and i < temp[-1] and(not i in temp):
                    temp.append(i)
                    self.gen(s, index+1, temp)
                    temp.pop(-1)
                if not self.ret is None:
                    return
                
    def smallestNumber(self, pattern: str) -> str:
        # self.solved = False
        self.ret = None
        self.gen(pattern, 0, [])
        return self.ret
