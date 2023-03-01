class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        cur = defaultdict(int)
        ans = 0
        maxChar = 0
        
        for right in range(len(s)):
            cur[s[right]] += 1
            maxChar = max(maxChar,cur[s[right]])
            
            while right - left + 1 - maxChar > k:
                cur[s[left]] -= 1
                left += 1
            ans = max(ans,right-left + 1)
        return ans
        