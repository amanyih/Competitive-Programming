class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = {i:i for i in range(1,len(edges)+1)}
        
        def getParent(a):
            cur = a
            count = 1
            while cur != graph[cur]:
                count += 1
                cur = graph[cur]
            
            return cur,count
        def isConnected(a,b):
            return getParent(a)[0] == getParent(b)[0]
        
        def join(a,b):
            ap,ac = getParent(a)
            bp,bc = getParent(b)
            
            if ac > bc:
                graph[ap] = bp
            else:
                graph[bp] = ap
        
        ans = edges[0]
        
        for a,b in edges:
            if isConnected(a,b):
                ans = [a,b]
            else:
                join(a,b)
        
        return ans
            
            
        