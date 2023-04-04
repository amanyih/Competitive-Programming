class Solution:
    def countArrangement(self, n: int) -> int:
        global bit
        global count
        count = 0
        bit = 0
        
        arr = [i+1 for i in range(n)]
        
        def check(path,cur):
            if not (len(path) +1) % cur:
                return True
            if not(cur % (len(path)+1)):
                return True
            return False
        
        def backtrack(path):
            global count
            global bit
            
            if len(path) == len(arr):
                count += 1
            
            for i in range(len(arr)):
                if not bit & 1<<i and check(path,arr[i]):
                    bit += 1<< i
                    path.append(arr[i])
                    backtrack(path)
                    path.pop()
                    bit -= 1<<i
        backtrack([])
        return count
                    
                    
        