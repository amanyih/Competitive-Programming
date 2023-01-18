class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid) - 1
        
        ans = []
        
        for i in range(1,n):
            row = []
            for j in range(1,n):
                tempMat = []
                tempMat.append(grid[i-1][j-1])
                tempMat.append(grid[i-1][j])
                tempMat.append(grid[i-1][j+1])
                tempMat.append(grid[i][j-1])
                tempMat.append(grid[i][j])
                tempMat.append(grid[i][j+1])
                tempMat.append(grid[i+1][j-1])
                tempMat.append(grid[i+1][j])
                tempMat.append(grid[i+1][j+1])
                row.append(max(tempMat))
            
            ans.append(row)
        
        return ans
                
        