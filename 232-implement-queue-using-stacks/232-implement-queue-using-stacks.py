class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if len(self.stack)!=0:
            tempStack = []
            for elements in range (len(self.stack)):
                tempStack.append(self.stack.pop())
            x = tempStack.pop()
            for elements in range (len(tempStack)):
                self.stack.append(tempStack.pop())
            
            return x
        
        
        

    def peek(self):
        return self.stack[0]
        """
        :rtype: int
        """
        

    def empty(self):
        if len(self.stack) != 0:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()