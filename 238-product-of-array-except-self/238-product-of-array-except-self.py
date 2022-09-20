class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1] * (len(nums)+1) #n
        
        for num in nums: #n
            pre.append(pre[-1] * num)
        
        for i in range(len(nums)-1,-1,-1):#n
            post[i] = post[i+1] * nums[i]
        ans = []
        
        for i in range(len(nums)):#n    O(4n) -- O(n)
            ans.append(pre[i]*post[i+1])
        
        return ans
        
            
            
        