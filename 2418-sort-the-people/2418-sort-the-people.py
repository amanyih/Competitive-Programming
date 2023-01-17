class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        _dict = defaultdict(list)
        maxHeight = max(heights)
        
        temp = [0]*(maxHeight+1)
        
        for i in range(len(names)):
            temp[heights[i]] = names[i]
        
        ans = []
        
        for i in range(len(temp)-1,-1,-1):
            if temp[i] != 0:
                ans.append(temp[i])
        
        return ans
        
        
                
            

        