class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        visited = set()
        count = 0
        
        
        def dfs(row,col):
            # print(row,col)
            
            
            visited.add((row,col))
            
            for direction in directions:
                r,c =direction
                
                if 0 <= row + r < len(grid) and 0 <= col + c < len(grid[0]) and (row+r,col+c) not in visited and grid[row+r][col+c] == "1":
                    dfs(row + r, col + c)
        
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == "1":
                    # print(r,c)
                    dfs(r,c)
                    count += 1
                
        
        return count
    
    """
    
    [["1","1","0","0","0"]
    ,["1","1","0","0","0"]
    ,["0","0","1","0","0"],
     ["0","0","0","1","1"]]
    
    """
        