class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        
        _dict = defaultdict(int)
        for col in (zip(*grid)):
            _dict[col] += 1
        
        ans = 0
        for row in grid:
            t = tuple(row)
            if t in _dict:
                ans += _dict[t]
                
        
        
        
        return ans
            
                
        
        
        