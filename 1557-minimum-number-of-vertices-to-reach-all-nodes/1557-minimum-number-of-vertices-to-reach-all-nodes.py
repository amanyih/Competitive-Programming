class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for edge in edges:
            f,t = edge
            graph[t].append(f)
        res = []
        for j in range(n):
            if not graph[j]:
                res.append(j)
        return res
                
        