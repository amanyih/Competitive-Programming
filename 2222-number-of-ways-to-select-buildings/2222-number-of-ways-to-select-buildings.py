class Solution:
    def numberOfWays(self, s: str) -> int:
        pattern = {"01":0,"10":0}
        zero = 0
        one = 0
        
        ans = 0
        
        for char in s:
            if char == "0":
                ans += pattern["01"]
                pattern["10"] += one
                zero += 1
            else:
                ans += pattern["10"]
                pattern["01"] += zero
                one += 1
        
        return ans
                
            