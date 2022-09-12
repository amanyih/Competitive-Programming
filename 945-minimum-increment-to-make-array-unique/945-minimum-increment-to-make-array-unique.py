class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        stack = []
        
        count = 0
        
        for num in nums:
            if stack and num <= stack[-1]:
                count += stack[-1] - num + 1
                num = stack[-1] + 1
            stack.append(num)
        
        return count
        