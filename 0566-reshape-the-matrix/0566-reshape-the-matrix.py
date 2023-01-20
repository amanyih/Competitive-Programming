class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        
        if(row*col != r*c):
            return mat
        
        ans = []
        newRow = []
        count = 0
        
        for ro in range(row):
            for co in range(col):
                newRow.append(mat[ro][co])
                count += 1
                
                if count % c == 0:
                    ans.append(newRow)
                    newRow = []
        
        return ans