OPERATORS = ['+', '-', '*', '/']
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in OPERATORS:
                op2 = stack.pop(-1)
                op1 = stack.pop(-1)
                match (token):
                    case '+': stack.append(op1+op2)
                    case '-': stack.append(op1-op2)
                    case '*': stack.append(op1*op2)
                    case '/': stack.append(int(op1/op2))
            else:
                stack.append(int(token))

        while len(stack) != 1:
            operator = stack.pop(-1)
            op2 = stack.pop(-1)
            op1 = stack.pop(-1)
            match (operator):
                case '+': stack.append(op1+op2)
                case '-': stack.append(op1-op2)
                case '*': stack.append(op1*op2)
                case '/': stack.append(op1//op2)
        return stack[-1]