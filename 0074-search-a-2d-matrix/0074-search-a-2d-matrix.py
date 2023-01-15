class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        col = len(matrix[0])
        row = len(matrix)
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == target:
                    return True
        
        return False