class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        global count1
        global count2
        count1 = 0
        count2 = 0
        
        def dfs(row,col):
            global count1
            global count2
            
            if grid1[row][col] == grid2[row][col]:
                count1 += 1
            count2 += 1
                
            
            visited.add((row,col))
            
            
            for direction in directions:
                r,c = direction
                
                newR = row + r
                newC = col + c
                
                if 0 <= newR < len(grid2) and 0 <= newC < len(grid2[0]) and (newR,newC) not in visited and grid2[newR][newC] == 1:
                    dfs(newR,newC)
                    
                    
                    
            return count1==count2
        
        ans = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i,j) not in visited and grid2[i][j] == 1:
                    count1 = 0
                    count2 = 0
                    if dfs(i,j):
                        
                        ans += 1
        return ans
    
            
            
        