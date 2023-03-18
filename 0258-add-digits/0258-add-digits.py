class Solution:
    def addDigits(self, num: int) -> int:
        
        
        def add(arr):
            if len(str(arr)) == 1:
                return arr
            
            newArr = [int(x) for x in str(arr)]
            return add(sum(newArr))
        
        return add(num)
        