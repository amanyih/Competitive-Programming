class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # 0 is water
        # 1 is land
        row = len(grid)
        col = len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        lands = set()
        q = deque()
        visited = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    q.append((i,j,0))
                    lands.add((i,j))
                    visited.add((i,j))
        
        def inBound(row,col):
            # print(row,col)
            # print(0 <= row < len(grid) and 0 <= col < len(grid[0]))
            
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        ans = -1
        # print(visited)
        
        
        while q:
            # print(visited)
            r,c,d = q.popleft()
            
            for a,b in directions:
                new_r,new_c = r + a,c + b
                if inBound(new_r,new_c) and (new_r,new_c) not in visited:
                    # print("00here")
                    visited.add((new_r,new_c))
                    grid[new_r][new_c] = d + 1
                    q.append((new_r,new_c,d+1))
        # print(grid)
        for i in range(row):
            for j in range(col):
                if (i,j) not in lands:
                    ans = max(ans,grid[i][j])
        return -1 if ans == 0 else ans
                
                
            
            
            
            
        
        