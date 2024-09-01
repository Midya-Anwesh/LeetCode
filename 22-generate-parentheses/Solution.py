# runtime = 57.0ms
# memory usage = 16.7MB

class Solution:
    def is_valid(self, s: list[str]) -> bool:
        stack, top = [None for i in range(len(s))], -1
        for ele in s:
            if ele == "(":
                stack[top:=top+1] = ele
            elif ele == ")" and top >= 0:
                top -= 1
            else:
                return False
        return top == -1

    def gen_sequence(self, n: int, s: list[str], index: int) -> None:
        if index == n-1:
            if self.is_valid(s):
                self.ret.append("".join(s.copy()))
            return
        for ele in ("(",")"):
            s[index] = ele
            self.gen_sequence(n, s, index+1)
            
    def generateParenthesis(self, n: int) -> List[str]:
        self.ret = []
        temp = [0 for i in range(2*n)]
        temp[0], temp[-1] = "(",")"
        self.gen_sequence(2*n, temp , 1)
        return self.ret