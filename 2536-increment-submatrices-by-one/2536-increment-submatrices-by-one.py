class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * (n+1) for i in range(n+1)]
        
        for query in queries:
            r1,c1,r2,c2 = query
            matrix[r1+1][c1+1]  += 1
            
            if c2 + 2 < n+1:
                matrix[r1+1][c2+2] -= 1
            if r2 + 2 < n+1:
                matrix[r2+2][c1+1] -= 1
            
            if r2 + 2 < n+1 and c2+2 < n+1:
                matrix[r2+2][c2+2] += 1
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix)):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j] - matrix[i-1][j-1] + matrix[i][j]
        matrix2 = []
        for i in range(1,len(matrix)):
            row = matrix[i][1:]
            matrix2.append(row)
        
        return matrix2
        
            
            
        
        
        
            