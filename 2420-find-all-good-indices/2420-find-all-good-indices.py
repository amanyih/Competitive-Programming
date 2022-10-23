class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
        stack = []
        forward = [False] * len(nums)
        
        for i,num in enumerate(nums):
            
            if len(stack) >= k:
                forward[i] = True
            
            if not stack:
                stack.append(num)
            
            else:
                
                if num <= stack[-1]:
                    stack.append(num)
                else:
                    stack = [num]
        stack = []
        ans = []
        for i in range(len(nums)-1,-1,-1):
            
            if len(stack) >= k and forward[i]:
                ans.append(i)
            if not stack:
                stack.append(nums[i])
            else:
                
                if nums[i] <= stack[-1]:
                    stack.append(nums[i])
                else:
                    stack = [nums[i]]
        
        return ans[::-1]
        