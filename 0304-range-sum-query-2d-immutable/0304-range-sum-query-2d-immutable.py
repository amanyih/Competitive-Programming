class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col = len(matrix[0])
        row = len(matrix)
        
        self.prefix = []
        
        for r in range(row+1):
            newCol = [0 for x in range(col +1)]
            self.prefix.append(newCol)
        prefixRow = len(self.prefix)
        prefixCol = len(self.prefix[0])
        
        for r in range(1,prefixRow):
            for c in range(1,prefixCol):
                self.prefix[r][c] = self.prefix[r][c-1] + self.prefix[r-1][c] + matrix[r-1][c-1] - self.prefix[r-1][c-1]
                            
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1]-self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)