class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = minSum = 0
        
        for num in nums:
            prefixSum += num
            minSum = min(prefixSum,minSum)
        
        return 1 - minSum if minSum < 1 else 1
        
        
        
        