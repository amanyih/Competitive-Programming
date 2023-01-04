class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        ans = []
        row = len(mat) -1
        column = len(mat[0]) - 1
        
        r = 0
        c = 0
        direction = 1 # direction 1 = going up, 0 going down
        
        
        for i in range((row+1)*(column+1)):
            ans.append(mat[r][c])
            
            if direction:
                if r > 0 and c < column:
                    r -= 1
                    c += 1
                elif c < column:
                    c += 1
                    direction = 0
                else:
                    r += 1
                    direction = 0
            else:
                if r < row and c > 0:
                    r += 1
                    c -= 1
                elif r < row:
                    r += 1
                    direction = 1
                else:
                    c += 1
                    direction = 1
        return ans
                
                
        
        
        
        
        
        
        
        