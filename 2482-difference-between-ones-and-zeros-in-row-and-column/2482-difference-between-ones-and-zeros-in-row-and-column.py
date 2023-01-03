class Solution:
    def onesMinusZeros(self, mat: List[List[int]]) -> List[List[int]]:
        prefix = []
        
        for i in range(len(mat)):
            prefix.append([])
            for j in range(len(mat[i])):
                prevA = prefix[i-1][j] if i > 0 else 0
                prevS= prefix[i][j-1] if j > 0 else 0
                
                subt = prefix[i-1][j-1] if (j > 0 and i > 0) else 0
                cur = mat[i][j]
                
                prefix[i].append(prevA+prevS+cur-subt)
        
        ans = []
        lastI = len(mat)-1
        lastJ = len(mat[i])-1
        
        for i in range(len(mat)):
            ans.append([])
            for j in range(len(mat[i])):
                onesRow= prefix[i][lastJ] - prefix[i-1][lastJ] if i > 0 else prefix[i][lastJ]
                zerosRow = lastJ - onesRow + 1
                onesColumn = prefix[lastI][j] - prefix[lastI][j-1] if j > 0 else prefix[lastI][j]
                zerosColumn = lastI - onesColumn + 1
                
                ans[i].append(onesRow+onesColumn-zerosRow-zerosColumn)
        
        return ans
                
        