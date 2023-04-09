class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()
        
        ans = 0
        
        def explore(row,col,count):
            
            visited.add((row,col))
            count.append(1)
            
            for direction in directions:
                r,c = direction
                
                if 0 <= row + r < len(grid) and 0<= col + c < len(grid[0]) and grid[row+r][col+c] == 1 and (row+r,col+c) not in visited:
                    explore(row+r,col+c,count)
            return sum(count)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    cur = explore(r,c,[])
                    ans = max(ans,cur)
        
        return ans
            
            
            
            