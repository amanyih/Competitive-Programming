class Solution:
    def countHomogenous(self, s: str) -> int:
        
        
        # window = set()
        
        right= 0
        ans = 0
        MOD = 10 ** 9 + 7
        
        def count_sub_string(n):
            return n * (n+1) // 2
        
        
        while right < len(s):
            left = right
            while right<len(s) and s[left] == s[right]:
                right += 1
            
            count = count_sub_string(right - left)
            ans += count_sub_string(right - left)
            
        return ans % MOD
            
            
            
            
            
            