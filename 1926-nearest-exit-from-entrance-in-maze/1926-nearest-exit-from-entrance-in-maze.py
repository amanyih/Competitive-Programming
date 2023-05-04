class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        entrance = tuple(entrance)
        
        def inBound(row,col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        
        def isExit(row,col):
            
            return row == 0 or row == len(maze)-1 or col == len(maze[0])-1 or col ==0
        
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        
        q = deque([(entrance[0],entrance[1],0)])
        
        visited = set([entrance])
        
        while q:
            
            row,col,path = q.popleft()
            # isit = isExit(row,col)
            # print(row,col,isit)
            
            if isExit(row,col) and path:
                return path
            
            for direction in directions:
                r,c = direction
                new_r = row + r
                new_c = col + c
                
                if inBound(new_r,new_c) and (new_r,new_c) not in visited and maze[new_r][new_c] != "+":
                    visited.add((new_r,new_c))
                    q.append((new_r,new_c,path+1))
        
        return -1
        
         