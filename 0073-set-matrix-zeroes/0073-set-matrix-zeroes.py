class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        allColumns = set()
        allRows = set()
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    allColumns.add(c)
                    allRows.add(r)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in allRows or c in allColumns:
                    matrix[r][c] = 0
        
        