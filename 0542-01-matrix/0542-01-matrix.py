class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        ans = [[inf for i in range(len(mat[0]))] for j in range(len(mat))]
        
        def inBound(row,col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        q = deque()
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    ans[i][j] = 0
                    q.append((i,j,0))
        
        # print(q)
        while q:
            
            row,col,count = q.popleft()
            
            for direction in directions:
                r,c = direction
                new_r = row + r
                new_c = col + c
                
                if inBound(new_r,new_c) and mat[new_r][new_c] != 0:
                    cur = ans[new_r][new_c]
                    if count + 1 < cur:
                        ans[new_r][new_c] = min(count+1,cur)
                        q.append((new_r,new_c,count+1))
        # print(ans)
        return ans
                
        
        
        