class Solution(object):
    def validateStackSequences(self, pushed, popped):
        left = 0
        stack = []
        
        for index in range(len(pushed)):
            stack.append(pushed[index])
            
            while stack and stack[-1] == popped[left]:
                stack.pop()
                left += 1
        
        return False if stack else True
        