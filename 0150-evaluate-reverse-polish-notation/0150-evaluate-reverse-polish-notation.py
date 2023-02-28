class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {"+","-","/","*"}
        stack = []
        
        for token in tokens:
            if token in ops:
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                
                stack.append(int(eval(str(firstOperand) + token+str(secondOperand))))
            else:
                stack.append(int(token))
        
        return sum(stack)
                
        