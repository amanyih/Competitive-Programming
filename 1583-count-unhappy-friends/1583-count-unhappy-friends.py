class Solution:
    def unhappyFriends(self, n: int, prefs: List[List[int]], pairs: List[List[int]]) -> int:
        
        prefTable = [[0]*n for i in range(n)]
        pairMap = {}
        
        for i in range(len(prefs)):
            for j in range(len(prefs[0])):
                p = prefs[i][j]
                prefTable[i][p] = n-1-j
        
        for x,y in pairs:
            pairMap[x] = y
            pairMap[y] = x
        count = 0
        for x in pairMap:
            y = pairMap[x]
            x_y = prefTable[x][y]
            isUnhappy = False
            
            for u in range(n):
                if u != y:
                    x_u = prefTable[x][u]
                    u_x = prefTable[u][x]
                    v = pairMap[u]
                    u_v = prefTable[u][v]
                    
                    if x_u > x_y and u_x > u_v:
                        isUnhappy = True
            if isUnhappy:
                count += 1
        return count
                
                
                
            
            
        
                
        
        