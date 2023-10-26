class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def findLand():
            rows = len(grid)
            cols = len(grid[0])

            for row in range(rows):
                for col in range(cols):
                    if grid[row][col]:
                        return row,col
        def isValid(row,col):
            r = len(grid)
            c = len(grid[0])
            
            return 0 <= row < r and 0 <= col < c
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        land = findLand()
        
        q = deque([land])
        
        visited = set()
        visited.add(land)
        
        ans = 0
        while q:
            # print(q,visited)
            cur_r,cur_c = q.popleft()
            
            for r,c in directions:
                new_r,new_c = cur_r+r,cur_c + c
                is_valid = isValid(new_r,new_c) and grid[new_r][new_c] == 1
                # print(new_r,new_c,is_valid)
                if not is_valid:
                    # print(new_r,new_c)
                    ans += 1
                if is_valid and (new_r,new_c) not in visited:
                    q.append((new_r,new_c))
                    visited.add((new_r,new_c))
            # print(ans)
        return ans
                    
                
                
        
        
                
        