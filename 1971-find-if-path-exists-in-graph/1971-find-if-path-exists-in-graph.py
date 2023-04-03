class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for edge in edges:
            start,end = edge
            graph[start].append(end)
            graph[end].append(start)
        
        # print(graph)
        def isValidPath(graph,source,destination):
            stack = [source]
            visited = set()
            
            while stack:
                cur = stack.pop()
                if cur == destination:
                    return True
                visited.add(cur)
                for neigh in graph[cur]:
                    if neigh not in visited:
                        stack.append(neigh)
            return False
        
        return isValidPath(graph,source,destination)
            
            