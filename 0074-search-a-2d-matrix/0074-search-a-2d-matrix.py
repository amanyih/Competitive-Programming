class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if len(matrix) == 1 and len(matrix[0]) == 1:
            if matrix[0][0] == target:
                return True
            return False
        colLength = len(matrix[0])
        left = 0
        right = (len(matrix) -1) * colLength + colLength-1
        # print(left,right)
        
        while left < right:
            middle = (left + right) // 2
            
            curCol = middle % colLength
            curRow = middle // colLength
            
            if matrix[curRow][curCol] == target:
                return True
            elif matrix[curRow][curCol] > target:
                right = middle
            else:
                left = middle +1
        if left == right:
            middle = (left + right) // 2
            
            curCol = middle % colLength
            curRow = middle // colLength
            if matrix[curRow][curCol] == target:
                return True
            
        return False