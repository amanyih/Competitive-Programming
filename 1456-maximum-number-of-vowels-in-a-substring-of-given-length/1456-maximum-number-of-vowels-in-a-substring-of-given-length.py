class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel = {"a","e","i","o","u"}
        
        
        ans = 0
        cur = 0
        left = 0
        
        
        for right in range(len(s)):
            
            cur += 1 if s[right] in vowel else 0
            
            if right - left + 1 == k:
                ans = max(ans,cur)
                if s[left] in vowel:
                    cur -= 1
                left += 1
        
        return ans
        