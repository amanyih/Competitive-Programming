class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [[1]]
        
        for i in range(1,numRows):
            cur = [1]
            last = ans[-1]
            
            for j in range(1,len(last)):
                cur.append(last[j-1]+last[j])
            cur.append(1)
            ans.append(cur)
        
        return ans
        
        
        
        
        
        
            
            
            
        