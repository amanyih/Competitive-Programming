class MinStack:

    def __init__(self):
        self.stack = []
        self.monStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.monStack or val <= self.monStack[-1]:
            self.monStack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if self.monStack and self.monStack[-1] == val:
            self.monStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.monStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()