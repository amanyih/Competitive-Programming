class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
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
        for i in range(len(mat)):
            ans.append([])
            for j in range(len(mat[i])):
                smallI = i-k if (i-k) >= 0 else 0
                bigI = i + k if (i + k) < len(mat) else len(mat) - 1
                
                smallJ = j - k if (j-k) >= 0 else 0
                bigJ =j+k if (j+k) < len(mat[i]) else len(mat[i]) - 1
                
                maxSum = prefix[bigI][bigJ]
                left = prefix[bigI][smallJ-1] if smallJ > 0 else 0
                above = prefix[smallI-1][bigJ] if smallI > 0 else 0
                extra = prefix[smallI-1][smallJ-1] if (left != 0 and above !=0) else 0
                
                ans[i].append(maxSum-left-above+extra)
        
        return ans
                    
        
        
        
        