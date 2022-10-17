class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        count = {0:-1}
        
        cur = 0
        
        ans = 0
        
        for i,num in enumerate(nums):
            
            cur += 1 if num == 1 else -1
            
            if cur in count:
                
                ans = max(ans,i-count[cur])
                
            else:
                
                count[cur] = i
        
        return ans