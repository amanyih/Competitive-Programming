class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])
        m = len(grid)
        
        [1,2,3]
        [4,5,6]
        
        
        
        for row in range(m-2,-1,-1):
            grid[row][-1] += grid[row+1][-1]
            
        for col in range(n-2,-1,-1):
            grid[-1][col] += grid[-1][col+1]
        
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                grid[i][j] += min(grid[i][j+1], grid[i+1][j])
        # print(grid)
        return grid[0][0]
        