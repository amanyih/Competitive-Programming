class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        
        stack =[]
        ansLst=[0] * len(temps)
        
        for i,num in enumerate(temps):
            while stack and num > temps[stack[-1]]:
                index = stack.pop()
                ansLst[index] = i - index
            stack.append(i)
        
        return ansLst
            
            
        
        # 0  1  2  3  4  5  6  7
        #[73,74,75,71,69,72,76,73]
        #[1,1,4,2,1,1,0,0]
       
        