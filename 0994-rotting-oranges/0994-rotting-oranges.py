class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def getRotten():
            lst = []
            tom =[]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        lst.append((i,j))
                    elif grid[i][j] ==1:
                        tom.append((i,j))
                        
            return lst,tom
        def isBound(row,col):
            return 0 <= row < len(grid) and  0 <= col < len(grid[0])
        rotten,tom = getRotten()
        if not rotten and tom:
            return -1
        elif not rotten:
            return 0
        
        q = deque(rotten)
        visited = set()
        
        count = -1
        
        while q:
            count += 1
            
            newLst = []
            
            for orange in q:
                row,col = orange
                for direction in directions:
                    r,c = direction
                    new_r = row + r
                    new_c = col + c
                    
                    if isBound(new_r,new_c) and (new_r,new_c) not in visited and grid[new_r][new_c] == 1:
                        newLst.append((new_r,new_c))
                        visited.add((new_r,new_c))
            q = deque(newLst)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    return -1
        return count
                        
                    
            