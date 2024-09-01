# runtime = 1159.0ms
# memory usage = 16.5MB

class Solution:
    def __init__(self):
        self.temp = []
        self.ret = set()
        self.solved = False

    def is_valid(self, s, length):
        t, st, e = [], 0, length-1
        while(st in self.temp and st < length-1):
            st += 1
        while(e in self.temp and e > 0):
            e -= 1
        # print(st, e)
        if s[st] == ")" or s[e] == "(":
            return False
        for i in range(len(s)):
            if i in self.temp or (s[i] >= "a" and s[i] <= "z"):
                continue
            if s[i] == "(" or len(t) == 0:
                t.append(s[i])
            elif s[i] == ")" and len(t) > 0 and t[-1]=="(":
                t.pop(-1)
            else:
                return False
        return not len(t)

    def gen(self, s, length, cut, si = 0, l = 0):
        if cut == l:
            if self.is_valid(s, length):
                # print( "".join( [s[i] for i in range(length) if not i in self.temp] ) )
                self.ret.add("".join( [s[i] for i in range(length) if not i in self.temp] ))
                self.solved = True
            return
        for i in range(si, length):
            if s[i] == "(" or s[i] ==")":
                self.temp.append(i)
                self.gen(s, length, cut, i+1, l+1)
                self.temp.pop(-1)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        op, cl, length = 0,0, len(s)
        for i in range(length):
            if s[i] == "(":
                op += 1
            elif s[i] == ")":
                cl += 1
        if not op or not cl:
            s1 = ""
            for i in range(length):
                if s[i] != "(" and s[i] != ")":
                    s1 += s[i]
            return [s1]
        # length = len(s)
        for i in range(abs(op-cl), length):
            self.gen(s, length, i)
            if self.solved:
                break
        return self.ret if self.solved else [""]