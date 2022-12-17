class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        ans = [[] for _ in matrix[0]] 
        
        for row in matrix:
            for i in range(len(row)):
                # print(row[i])
                ans[i].append(row[i])
        
        return ans
        