class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        # Time Complexity = O(n*m) 
        #         where n = number of columns
        #               m = number of rows
        #     space complexity = O(1)
        
                
        col = len(matrix[0])
        row = len(matrix)
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == target:
                    return True
        
        return False