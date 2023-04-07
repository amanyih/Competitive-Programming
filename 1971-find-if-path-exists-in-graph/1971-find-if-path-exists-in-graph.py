class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node,target,visited):
            
            
            if node == target:
                return True
            
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    
                    if dfs(neighbour,target,visited):
                        return True
            return False
        
        return dfs(source,destination,set())
        
            
            