class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        maxAvg = -inf
        curSum = 0
        left = 0
        
        for right in range(len(nums)):
            curSum += nums[right]
            
            if right -left + 1 == k:
                curAvg = curSum/k
                maxAvg = max(maxAvg,curAvg)
                curSum -= nums[left]
                left += 1
        
        return maxAvg
            
        


