class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        for i in range(len(nums)):
            if prefix[i] == prefix[-1] - prefix[i+1]:
                return i
        
        return -1
        