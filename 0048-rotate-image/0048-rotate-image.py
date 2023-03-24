class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        left = top = 0
        right,bottom = len(matrix[0])-1,len(matrix)-1
        
        while left <= right:
            t,b,l,r = top,bottom,left,right
            
            while t < bottom:
                onTop,onBottom,onLeft,onRight = matrix[top][l],matrix[bottom][r],matrix[b][left],matrix[t][right]
                matrix[top][l],matrix[bottom][r],matrix[b][left],matrix[t][right] = onLeft,onRight,onBottom,onTop
                
                t,b,l,r = (t+1,b-1,l+1,r-1)
            
                
            top,bottom,left,right = (top+1,bottom-1,left+1,right-1)
        
        
        
        