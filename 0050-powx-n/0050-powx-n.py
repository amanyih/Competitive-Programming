class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def calculate(x,n):
            if n == 1:
                return x
            elif n == 0:
                return 1
            
            if n % 2 == 0:
                num = calculate(x,n//2)
                return num * num
            else:
                num = calculate(x,n-1)
                return x * num
        mul = calculate(x,abs(n))
        
        if n >= 0:
            return mul
        
        return 1/mul