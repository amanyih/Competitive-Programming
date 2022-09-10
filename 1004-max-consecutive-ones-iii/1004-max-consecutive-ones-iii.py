class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        maxOne = 0
        zeros = 0
        
        for right in range(len(nums)):
            if nums[right] == 0 and zeros <= k:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxOne = max(maxOne,right-left+1)
        
        return maxOne
                    
                
            