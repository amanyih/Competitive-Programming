class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ansList = [0]*len(temp)
        
        for index,num in enumerate(temp):
            while stack and temp[stack[-1]] < num:
                ansList[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        
        return ansList
        
        
        
        