class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        def inBound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid)
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()
        target = (len(grid)-1,len(grid)-1)
        
            
        
        
        heap = [(grid[0][0],(0,0))]
        
        while heap:
            weight,node = heappop(heap)
            visited.add(node)
            if node == target:
                return weight
            
            for r,c in directions:
                row,col = node
                new_r,new_c = r + row,col + c
                if inBound(new_r,new_c) and (new_r,new_c) not in visited:
                    cur_max = max(grid[new_r][new_c],weight)
                    heappush(heap,(cur_max,(new_r,new_c)))
                    visited.add((new_r,new_c))
                
                
                
            
            
        