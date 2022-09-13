class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            return recursion(x*x,n//2) if not n % 2 else x * recursion(x*x,n//2)
        
        ans = recursion(x,abs(n))
        return ans if n >= 0 else 1/ans
            