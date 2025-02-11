class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = ""
        for char in s:
            stack += char
            if stack[-len(part):] == part:
                stack = stack[:-len(part)]
        return stack