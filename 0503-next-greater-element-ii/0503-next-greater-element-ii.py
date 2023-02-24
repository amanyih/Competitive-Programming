class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        totalLoops = n * 2
        
        res = [-1]*n
        stack = []
        
        for i in range(totalLoops):
            index = i % n
            while stack and nums[stack[-1]] < nums[index]:
                curIndex = stack.pop()
                if res[curIndex] == -1:
                    res[curIndex] = nums[index]
            stack.append(index)
        
        return res
            
        