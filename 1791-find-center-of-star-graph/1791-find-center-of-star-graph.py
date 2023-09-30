class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for node in graph:
            if len(graph[node]) >1:
                return node
        