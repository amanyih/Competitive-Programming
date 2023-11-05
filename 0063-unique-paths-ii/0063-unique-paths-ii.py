class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        grid = [[1-obstacleGrid[j][i] for i in range(n)] for j in range(m)]
        
        for r in range(m-2,-1,-1):
            grid[r][-1] = min(grid[r][-1], grid[r+1][-1])
        for c in range(n-2,-1,-1):
            grid[-1][c] = min(grid[-1][c],grid[-1][c+1])
            
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if not obstacleGrid[i][j]:
                    grid[i][j] = grid[i][j+1] + grid[i+1][j]
                else:
                    grid[i][j] = 0
        # print(grid)
        return grid[0][0]