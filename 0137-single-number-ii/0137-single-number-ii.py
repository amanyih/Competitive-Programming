class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        first = 0
        second = 0
        
        for num in nums:
            first = (first ^ num) & (~second)
            second = (second ^ num) & (~first)
        return first ^ second
        