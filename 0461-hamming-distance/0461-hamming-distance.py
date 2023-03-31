class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y 
        count = 0
        mask = 1
        shift = 0
        
        while mask <= z:
            if mask & z !=0:
                count += 1
            shift += 1
            mask = 1<<shift
        return count
            