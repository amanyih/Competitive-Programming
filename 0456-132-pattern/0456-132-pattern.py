class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        curMin = nums[0]
        stack = []

        for num in nums:

            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack and num > stack[-1][1]:
                return True
            
            stack.append([num,curMin])
            curMin = min(curMin,num)
        
        return False

