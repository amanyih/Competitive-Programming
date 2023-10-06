class Solution:
    def knightDialer(self, n: int) -> int:
        
        directions = [(2,-1),(2,1),(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2)]
        MOD = 10 ** 9 +7
        cache = {}
        
        def is_valid(row,col):
            return 0 <= row < 4 and 0 <= col < 3 and (row,col) != (3,0) and (row,col) != (3,2)
        
        def dial(n,row,col):
            if (n,row,col) in cache:
                return cache[(n,row,col)]
            if n == 1:
                return 1
            cur_total = 0
            for r,c in directions:
                new_r = row + r
                new_c = col + c
                if is_valid(new_r,new_c):
                    cur_total += dial(n-1,new_r,new_c)
            cache[(n,row,col)] = cur_total
            return cur_total
        total = 0
        for i in range(4):
            for j in range(3):
                # print(is_valid(i,j),(i,j))
                if is_valid(i,j):
                    cur = dial(n,i,j)
                    # print((i,j),cur)
                    total += dial(n,i,j)
                    
                
        return total % MOD
                    
            
        
        
        
        
        