class Solution:
    def rob(self, nums: List[int]) -> int:
        anc = 0
        prev = 0      
        for num in nums:
            temp = prev
            prev = max(anc+num,prev)
            anc = temp
        return max(anc,prev)
        
        
        