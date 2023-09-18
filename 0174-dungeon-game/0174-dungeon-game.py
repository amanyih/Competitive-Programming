class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r  = len(dungeon)
        c = len(dungeon[0])
        
        cache = [[inf] * c for _ in range(r) ]
        
        cache[r-1][c-1] = max(1,1-dungeon[r-1][c-1])
        
        for i in range(c-2,-1,-1):
            cache[r-1][i] = max(1,cache[r-1][i+1]-dungeon[r-1][i])
        for i in range(r-2,-1,-1):
            cache[i][c-1] = max(1,cache[i+1][c-1] - dungeon[i][c-1])
            
        
        # print(cache)
        
        
        for i in range(r-2,-1,-1):
            for j in range(c-2,-1,-1):
                cur = min(max(1,cache[i+1][j] - dungeon[i][j]),max(1,cache[i][j+1]-dungeon[i][j]))
                cache[i][j] = 1 if cur  <= 0 else cur
        return cache[0][0]
            
        
        