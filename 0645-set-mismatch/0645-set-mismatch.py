class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        count = {}
        
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        ans = [0,0]
        
        # print(count)
        
        for i in range(1,len(nums)+1):
            
            if i in count and count[i] == 2:
                ans[0] = i
            elif i not in count:
                ans[1] = i
            
            if ans[0] != 0 and ans[1] != 0:
                return ans
            
                
            
            
            
            
            
            
        