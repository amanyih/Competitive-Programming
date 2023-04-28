class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        
        if grid[0][0] or grid[n][n]: return -1
         
        def isBound(row,col): 
            return 0 <= row < len(grid) and 0 <= col < len(grid) 
        
        q = deque([(0,0,1)])
        
        directions = [(0,1),(1,1),(-1,1),(1,0),(-1,0),(1,-1),(0,-1),(-1,-1)]
        
        visited = set()
        visited.add((0,0))
        
        while q: 
            cur = q.popleft()
            row,col,count = cur
            
            if (row,col) == (n,n):
                return count
            
            visited.add((row,col))
            
            for direction in directions:
                r,c = direction
                new_r = row + r
                new_c = col + c
                
                if (new_r,new_c) not in visited and isBound(new_r,new_c) and grid[new_r][new_c] == 0:
                    visited.add((new_r,new_c))
                    q.append((new_r,new_c,count+1))
        return -1
                
                
            
            
        
        
        