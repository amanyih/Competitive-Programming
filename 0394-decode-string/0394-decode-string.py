class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if char  == "]":
                chars = []
                
                while stack[-1] != "[":
                    chars.append(stack.pop())
                
                stack.pop()
                numbers = []
                
                while stack and ord(stack[-1]) - ord("0") <= 9:
                    numbers.append(stack.pop())
                chars.reverse()
                numbers.reverse()
                num = int("".join(numbers)) if numbers else 0
                string = "".join(chars)
                if num:
                    for i in range(len(string)*num):
                        stack.append(string[i%len(string)])
                else:
                    for i in range(len(string)):
                        stack.append(string[i])
            else:
                stack.append(char)
        
        return "".join(stack)
        