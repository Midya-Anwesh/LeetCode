class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                to_mul = ""
                while stack[-1] != "[":
                    to_mul = stack.pop(-1)+to_mul
                stack.pop(-1)
                factor = ""
                while len(stack) and stack[-1].isdigit():
                    factor = stack.pop() + factor
                stack.append(to_mul*int(factor))
            else:
                stack.append(char)
        return "".join(stack)