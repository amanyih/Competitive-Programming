class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        for i in range(len(matrix) - 2,-1,-1):
            for j in range(len(matrix[0])):
                cur = matrix[i+1][j]
                if j > 0:
                    cur = min(cur,matrix[i+1][j-1])
                    
                if j + 1 < len(matrix[0]):
                    cur = min(cur,matrix[i+1][j+1])
                matrix[i][j] += cur
        
        return min(matrix[0])
        