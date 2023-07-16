class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = 0
        
        def count(s,left,right):
            ans = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1
            return ans
            
        
        for i in range(len(s)):
            left = right = i
            
            ans += count(s,left,right)
            left,right = i,i+1
            ans += count(s,left,right)
        
        return ans
            
                
        