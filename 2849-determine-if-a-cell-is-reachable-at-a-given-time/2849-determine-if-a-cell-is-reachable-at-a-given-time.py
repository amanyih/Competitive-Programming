class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx,sy) == (fx,fy) and t == 1:
            return False
        
        min_distance = max(abs(sx-fx),abs(sy-fy))
        
        return min_distance <= t
        
        
        