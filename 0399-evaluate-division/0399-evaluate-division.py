class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for i,equation in enumerate(equations):
            a,b = equation
            value = values[i]
            graph[a].append((b,value))
            graph[b].append((a,1/value))
        # print(graph)
        
        def dfs(start,destination,visited):
            # print(start,destination)
            
            if start == destination:
                return 1
            visited.add(start)
            for node in graph[start]:
                nxt,val = node
                if nxt not in visited:
                    res = dfs(nxt,destination,visited)
                    if res > -1:
                        return val * res            
            return -1
        res = []
        for a,b in queries:
            if a not in graph or b not in graph:
                res.append(-1)
            else:
                res.append(dfs(a,b,set()))
        return res
            
            
            
            
            
            