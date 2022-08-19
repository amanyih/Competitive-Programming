class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for char in s:
            if stack:
                if stack[-1] == char:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return "".join(stack)
        