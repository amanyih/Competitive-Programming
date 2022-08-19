class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        charlist = ["*","/","+","-"]
        stack = []
        for char in tokens:
            if char not in charlist:
                stack.append(char)
            else:
                x,y = stack.pop(),stack.pop()
                stack.append(str(int(eval(y+char+x ))))

        return int(stack[0])
        