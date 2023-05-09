class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        
        
        def findOne():
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if grid[i][j]:
                        return (i,j)
        def isBound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid)
        
        def dfs(start):
            visited.add(start)
            
            
            row,col = start
            
            for direction in directions:
                r,c = direction
                
                new_r = row + r
                new_c = col + c
                
                if isBound(new_r,new_c) and (new_r,new_c) not in visited and grid[new_r][new_c]:
                    dfs((new_r,new_c))
        
        intial = findOne()
        dfs(intial)
        first = list(visited)
        
        q = deque([(r,c,0) for r,c in first])
        new_visted = set()
        # print("fist",len(first))
        
        while q:
            
            cur = q.popleft()
            row,col,path = cur
            
            if grid[row][col] and (row,col) not in visited:
                return path - 1
            
            for direction in directions:
                r,c = direction
                new_r = row+r
                new_c = col+c
                
                if isBound(new_r,new_c) and (new_r,new_c) not in visited and (new_r,new_c) not in new_visted:
                    new_visted.add((new_r,new_c))
                    q.append((new_r,new_c,path+1))
                
            
        
        
        
        
        