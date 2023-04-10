class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        colors = {}
        
        
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        
        def dfs(cur,color):
            colors[cur] = color
            
            for n in graph[cur]:
                if n in colors:
                    if colors[n] == color:
                        return False
                
                else:
                    if not dfs(n,1-color):
                        return False
            return True
        
        
        for i in range(1,n+1):
            if i not in colors:
                if not dfs(i,0):
                    return False
                    
        return True
        