class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        num1Lst = num1.split("+")
        num2Lst = num2.split("+")
        num1Lst[0] = int(num1Lst[0])
        num1Lst[1] = int(num1Lst[1][:-1])
        
        num2Lst[0] = int(num2Lst[0])
        num2Lst[1] = int(num2Lst[1][:-1])
        
        real = []
        imaginary = []
        real.append(num1Lst[0]*num2Lst[0])
        real.append(num1Lst[1]*num2Lst[1]*-1)
        
        imaginary.append(num1Lst[0]*num2Lst[1])
        imaginary.append(num2Lst[0]*num1Lst[1])
        
        real = str(sum(real))
        imaginary = str(sum(imaginary))
        
        return real + "+" +imaginary + "i"
        
        
        