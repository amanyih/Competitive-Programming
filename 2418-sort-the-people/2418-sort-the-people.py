class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(1,len(names)):
            j = i -1
            cur = heights[i]
            curName = names[i]
            
            while j > -1 and heights[j] < cur:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j-=1
            
            heights[j+1] = cur
            names[j+1] = curName
        
        return names
                
            

        