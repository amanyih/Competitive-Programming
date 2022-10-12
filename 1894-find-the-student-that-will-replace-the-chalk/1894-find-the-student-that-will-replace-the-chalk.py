class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = sum(chalk)
        
        remainder = k % total
        
        for i,value in enumerate(chalk):
            
            if value > remainder:
                return i
            else:
                remainder -= value
        