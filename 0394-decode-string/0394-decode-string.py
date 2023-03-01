class Solution:
    def decodeString(self, s: str) -> str:
        if "[" not in s:
            y = ""
            p = 0
            while p < len(s):
                if s[p].isalpha():
                    y += s[p]
                p += 1
            return y
                    
        
        
        stack = []
        
        left = 0
        curChars = ""
        number = ""
        while left < len(s):
            if s[left].isalpha():
                l = left
                while l < len(s) and s[l].isalpha():
                    curChars += s[l]
                    l += 1
                left = l
                stack.append(curChars)
                curChars = ""
            elif s[left] == "[":
                stack.append("[")
                left += 1
            elif s[left] != "]":
                while s[left].isalnum() and not s[left].isalpha() and s[left] != "]":
                    number += s[left]
                    left += 1
                stack.append(int(number))
                number = ""
            else:
                curParameter = ""
                while stack and stack[-1] != "[":
                    curParameter = stack.pop() + curParameter
                if stack:
                    stack.pop()
                    num = stack.pop()
                    something = self.decodeString(num*curParameter)
                    stack.append(something)
                left += 1
        return "".join(stack)
            
                
            
        
        
        