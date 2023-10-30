class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        cache = {2 ** i : i for i in range(20)}
        
        def getPower(num):
            if num in cache:
                return cache[num]
            
            
            if num % 2:
                count = getPower(3*num + 1)
            else:
                count = getPower(num//2)
            
            count += 1
            cache[num] = count
            return count
        
        arr = [x for x in range(lo,hi+1)]
        
        arr.sort(key = lambda num : (getPower(num),num))
        
        return arr[k-1]