class MyQueue:

    def __init__(self):
        self.top = 0
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        ret = self.stack[self.top]
        self.top += 1
        return ret

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.stack[self.top]

    def empty(self) -> bool:
        return self.top >= len(self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()