class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = {"+","/","*","-"}
        currentNum = ""
        lastSign = "+"
        for char in s:
            if char.isalnum():
                currentNum += char
            elif not char.isalnum() and char in sign:
                if lastSign == "*":
                    stack.append(stack.pop()*int(currentNum))
                elif lastSign == "/":
                    stack.append(int(stack.pop()/int(currentNum)))
                elif lastSign == "-":
                    stack.append(int(currentNum)*-1)
                else:
                    stack.append(int(currentNum))
                currentNum = ""
                lastSign = char
        if lastSign == "*":
            stack.append(stack.pop()*int(currentNum))
        elif lastSign == "/":
            stack.append(int(stack.pop()/int(currentNum)))
        elif lastSign == "-":
            stack.append(int(currentNum)*-1)
        else:
            stack.append(int(currentNum))
        
        
        
        ans = 0
        for num in stack:
            ans += num
        return ans
            
                
                
        
            
                
        
                