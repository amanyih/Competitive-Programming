class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        longest = 0
        
        for i in range(len(s)):
            # print(s[i])
            left = right = i
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                if longest < right - left + 1:
                    ans = s[left:right+1]
                    longest = right - left  + 1
                
                left -= 1
                right += 1
            
            left,right = i,i+1
            while left >= 0 and right < len(s) and s[left] == s[right] :
                
                if longest < right - left + 1:
                    ans = s[left:right+1]
                    longest = right - left  + 1
                
                left -= 1
                right += 1
        
        return ans
        