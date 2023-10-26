class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def valid(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        visited = set()
        
        def dfs(row,col,cur_visited):
            cur_visited.add((row,col))
            
            for r,c in directions:
                new_r,new_c = row + r, col + c
                if valid(new_r,new_c) and grid[new_r][new_c] and (new_r,new_c) not in cur_visited:
                    cur_visited.add((new_r,new_c))
                    dfs(new_r,new_c,cur_visited)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j ) not in visited:
                    cur_visited = set()
                    dfs(i,j,cur_visited)
                    # print(i,j,len(cur_visited))
                    ans = max(ans,len(cur_visited))
                    visited = visited.union(cur_visited)
        return ans
                    
                    
            
        
        
        
        