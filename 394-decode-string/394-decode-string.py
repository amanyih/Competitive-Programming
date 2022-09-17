class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i !=  "]":
                stack.append(i)
            else:
                word = ""
                while stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                num = ""
                while stack and stack[-1].isalnum() and not stack[-1].isalpha():
                    num = stack.pop() + num
                num = int(num)
                word = num * word
                
                for char in word:
                    stack.append(char)
        return "".join(stack)
        