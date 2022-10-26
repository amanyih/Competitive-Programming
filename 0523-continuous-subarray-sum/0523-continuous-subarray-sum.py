class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        remainders = {0:0}
        
        prefix = 0
        
        for index in range(len(nums)):
            prefix += nums[index]
            
            if prefix % k not in remainders:
                remainders[prefix % k] = index +1
            elif remainders[prefix%k] < index:
                return True
                
        
        return False