class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = []
        for row in matrix:
            summ = 0
            newRow = []
            for i in range(len(row)):
                summ+=row[i]
                newRow.append(summ)
            self.prefix.append(newRow)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1,row2+1):
            val1 = self.prefix[i][col1] - self.matrix[i][col1]
            val2 = self.prefix[i][col2]
            ans += (val2-val1)
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)