class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        temp = []
        for num in nums:
            # print(num,temp)
            
            while temp and num - temp[0][0] > 1:
                cur = heappop(temp)
                
                if cur[1] < 3:
                    # print("from here")
                    return False
            if not temp:
                heappush(temp,[num,1])
            else:
                cur,count = heappop(temp)
                if cur + 1 == num:
                    heappush(temp,[num,count + 1])
                else:
                    heappush(temp,[cur,count])
                    heappush(temp,[num,1])
        for num,count in temp:
            if count < 3:
                print("from here")
                return False
        
        return True
                
                
            
            
                
                    
                
            
                
            
        