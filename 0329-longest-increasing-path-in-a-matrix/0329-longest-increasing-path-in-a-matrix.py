class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        grid = matrix
        
        
        directions  = [(1,0),(-1,0),(0,1),(0,-1)]
        max_at_cell = defaultdict(list)
        visited = set()
        
        ans = 0
        
        def inBound(row,col):
            nonlocal grid
            
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(cur):
            nonlocal ans
            
            visited.add(cur)
            
            row,col = cur
            
            max_lst = []
            
            for direc in directions:
                r,c = direc
                new_r = row + r
                new_c = col + c
                
                if (new_r,new_c) in max_at_cell and matrix[new_r][new_c] > matrix[row][col]:
                    max_lst.append(max_at_cell[(new_r,new_c)])
                elif inBound(new_r,new_c) and (new_r,new_c) not in visited and matrix[new_r][new_c] > matrix[row][col]:
                    max_lst.append(dfs((new_r,new_c)))
            curr_max =  (max(max_lst) + 1) if max_lst else 1
            max_at_cell[(row,col)] = curr_max
            ans= max(ans,curr_max)
            
            return curr_max
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) not in visited:
                    dfs((i,j))
        # print(max_at_cell)
        return ans
                    
                    
                
            

            
        