class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
     
        for i in range(len(names)):
            flag = True
            for j in range(len(names)-i-1):
                if heights[j] < heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
                    names[j],names[j+1] = names[j+1],names[j]
                    flag = False
            if flag == True:
                return names
        return names
            
                    

        