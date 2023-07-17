class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for x in range(n)] for j in range(m)]
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                grid[i][j] = grid[i][j+1] + grid[i+1][j]
        
        return grid[0][0]
            