class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        cur = 0 if n % 2 else 1
        
        while n:
            if n % 2 != 1 - cur:
                return False
            cur = 1 - cur
            n >>= 1
        return True
        
        