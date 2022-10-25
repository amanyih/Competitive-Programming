class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        count = {}
        
        for num in nums:
            if num in count:
                return True
            else:
                count[num] = 1
        
        return False