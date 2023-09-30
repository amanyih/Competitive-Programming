class Solution:
    def validPath(self, n: int, edges: List[List[int]], sou: int, des: int) -> bool:
        
        graph = defaultdict(list)
        visited = set()
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        def find(sou,des):
            visited.add(sou)
            
            if sou == des:
                return True
            
            for node in graph[sou]:
                if node not in visited and find(node,des):
                    return True
            
            return False
        
        return find(sou,des)
        
            
            