class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        counts = {0:-1}
        count = 0
        ans = 0
        
        for i,value in enumerate(nums):
            count += 1 if value == 1 else -1
            
            if count in counts:
                ans = max(i-counts[count],ans)
            else:
                counts[count] = i
        
        return ans
            
        