class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        positive, negative = 1, 1
        
        if len(nums) < 2:
            return len(nums)
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                positive = negative + 1
            elif nums[i] < nums[i - 1]:
                negative = positive + 1
                
        return max(positive, negative)
            
            
        
        
        