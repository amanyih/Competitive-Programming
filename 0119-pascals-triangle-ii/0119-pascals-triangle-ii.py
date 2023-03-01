class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        above = self.getRow(rowIndex-1)
        current = []
        for i in range(1,rowIndex):
            current.append(above[i] + above[i-1])
        
        return [1] + current + [1]
            
        
        