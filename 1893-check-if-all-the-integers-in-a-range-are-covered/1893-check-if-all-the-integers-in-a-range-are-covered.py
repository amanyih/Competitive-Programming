class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for i in range(left,right+1):
            flag = False
            for rangee in ranges:
                if i >= rangee[0] and i <= rangee[1]:
                    flag = True
                    break
            if not flag: return False
        
        return True
            
            
        