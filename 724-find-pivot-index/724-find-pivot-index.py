class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        
        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[-1]+nums[i])
        
        for i in range(0,len(nums)):
            if prefixSum[-1]-prefixSum[i] == prefixSum[i] - nums[i]:
                return i
            elif (i == 0 and prefixSum[-1]-prefixSum[i] == 0) or (i == len(nums) - 1 and prefixSum[i] - nums[i] == 0):
                return i
        
        return -1
        