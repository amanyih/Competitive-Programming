class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        
        
        count = {}
        
        cur = 0
        ans = 0
        
        for num in nums:
            cur += num
            if cur == goal:
                ans += 1
            
            if cur >= goal:
                prev = cur - goal
                
                ans += count.get(prev,0)
            count[cur] = count.get(cur,0) + 1
        
        return ans