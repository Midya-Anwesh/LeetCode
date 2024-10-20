class Solution:
    def evaluate(self, operands: List[str], operator: str) -> str:
        if len(operands) == 1:
            if operator == "!":
                return not self.operator[operands[0]]
            return self.operator[operands[0]]
            
        match operator:
            case "&":
                return reduce(lambda op1, op2="t":self.operator[op1] &self.operator[op2], operands)
            case "|":
                return reduce(lambda op1, op2="f":self.operator[op1] |self.operator[op2], operands)

    def parseBoolExpr(self, expression: str) -> bool:
       self.operator = {"f": False, "t": True, True: True, False: False}
       stack = list()
       for char in expression:
            if char == ")":
                operands = list()
                while stack[-1] != "(":
                    if (val := stack.pop()) != ",":
                        operands.append(val)
                stack.pop()
                val = self.evaluate(operands, stack.pop())
                stack.append("t" if val else "f")
            else:
                stack.append(char)

       return self.operator[stack.pop()]