class Solution:
    def isBipartite(self, inputG: List[List[int]]) -> bool:
        
        graph = defaultdict(set)
        
        colors = {}
        
        
        for i in range(len(inputG)):
            adjacent = inputG[i]
            
            for n in adjacent:
                graph[i].add(n)
                graph[n].add(i)
        
        
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
        
        
        for i in range(len(inputG)):
            if i not in colors:
                if not dfs(i,0):
                    return False
        # print(graph)
        # print(colors)
        return True