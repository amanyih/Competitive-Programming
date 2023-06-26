class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        track = {}
        
        def help(num):
            if num in track: return track[num]
            if num <= 1:
                track[num] = num
                return num
            if not num % 2:
                track[num] = help(num//2)
                return track[num]
            else:
                track[num] = help(num//2) + help(num//2 + 1)
                return track[num]
            
        for i in range(n+1):
            help(i)
        
        ans = 0
        
        for key in track:
            ans = max(ans,track[key])
        return ans
            
                
                
            
            
        