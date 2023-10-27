class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_len = 0
        ans = (0,0)
        
        for i in range(len(s)):
            left = right = i
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    ans = (left,right)
                    max_len = right - left + 1
                left -= 1
                right += 1
            
                
            left ,right = i,i+1
            
            while left >=0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    ans = (left,right)
                    max_len = right - left + 1
                left -= 1
                right += 1
        l,r = ans
        
        return s[l:r+1]
            
            
            
            
            
        