class Solution:
    def minimumSum(self, num: int) -> int:
        lst = [x for x in str(num)]
        lst.sort()
        
        x = int(lst[0] + lst[2])
        y = int(lst[1] + lst[-1])
        
        return x+y
        