class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        MOD = 10 ** 9 + 7
        odds = ceil(n/2)
        evens = n // 2
        
        even_count = pow(5,odds,MOD)
        odd_count = pow(4,evens,MOD)
        
        return (even_count * odd_count ) % MOD