class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        """
         0   1  2  3 4 5
        [-1,-1,-1,-1,1,1]
        [-1,-2,-3,-4,-3,-2]
        sum = 1
        
        {0:-1,}
         
        """
        
        count = {0:-1}
        cur = 0
        ans = 0
        
        for i in range(len(hours)):
            if hours[i] > 8:
                cur += 1
            else:
                cur -= 1
            
            last = (cur - 1) if cur <= 0 else 0
            if last in count:
                ans = max(ans,i-count[last])
            if cur not in count:
                count[cur] = i
        
        return ans
                
            
            