class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        
        
        left = 0
        ans = 0

        for right in range(len(s)):
            most = 0
            count[s[right]] = count.get(s[right],0) +1
            
            for key in count:
                most = max(most,count[key])

            while right - left + 1 - most > k:
                count[s[left]] -= 1
                left += 1
            
            ans = max(ans,right-left + 1)
        
        return ans