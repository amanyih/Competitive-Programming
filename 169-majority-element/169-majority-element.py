class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        majorCandidate = None
        
        for num in nums:
            if count == 0:
                majorCandidate = num
            
            count += 1 if num == majorCandidate else -1
        
        return majorCandidate