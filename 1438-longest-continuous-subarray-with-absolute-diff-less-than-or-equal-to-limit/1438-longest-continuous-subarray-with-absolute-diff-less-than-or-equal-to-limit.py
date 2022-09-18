class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxStack = []
        minStack = []
        left = 0
        ans = 0
        
        for right in range(len(nums)):
            
            while maxStack and maxStack[-1] < nums[right]:
                maxStack.pop()
            while minStack and minStack[-1] > nums[right]:
                minStack.pop()
            
            maxStack.append(nums[right])
            minStack.append(nums[right])
            
            while maxStack[0] - minStack [0] > limit:
                if maxStack[0] == nums[left]:
                    maxStack.pop(0)
                if minStack[0] == nums[left]:
                    minStack.pop(0)
                
                left += 1
            
            ans = max(ans,right - left + 1)
        
        return ans