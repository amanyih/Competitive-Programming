class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s_count = Counter(s)
        t_count = Counter(t)
        
        ans = 0
        
        for key in s_count:
            
            diff = s_count[key] - t_count[key]
            
            if diff > 0:
                ans += diff
        
        return ans