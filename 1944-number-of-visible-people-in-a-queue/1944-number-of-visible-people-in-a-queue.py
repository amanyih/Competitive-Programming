class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = []
        stack = []
        
        for i in range(len(heights)-1,-1,-1):
            if i == len(heights) -1:
                stack.append(heights[i])
                ans.append(0)
            else:
                smallers = 0
                
                while stack and stack[-1] < heights[i]:
                    stack.pop()
                    
                    smallers += 1
                if stack:
                    smallers += 1
                ans.append(smallers)
                stack.append(heights[i])
        
        ans.reverse()
        return ans
        
        