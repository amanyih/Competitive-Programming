class Solution:
    def reverse(self, x: int) -> int:
        
        y = abs(x)
        reverse = 0
        while y > 0:
            reverse = reverse * 10 + y%10
            y = y // 10
        reverse = -1 * reverse if x < 0 else reverse
        
        if reverse<2**31-1 and reverse > -2**31:
            return reverse
        else:
            return 0
            
        
        
        
        