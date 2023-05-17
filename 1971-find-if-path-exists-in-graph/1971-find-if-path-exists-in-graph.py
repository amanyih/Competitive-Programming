class Solution:
    def validPath(self, n: int, edges: List[List[int]], sou: int, des: int) -> bool:
        
        graph = {i:i for i in range(n)}
        # print(graph)
        
        def getParent(node):
            cur = node
            
            while node != graph[node]:
                node = graph[node]
            return node
        def connect(a,b):
            ap = getParent(a)
            bp = getParent(b)
            
            graph[ap] = bp
        
        
        for a,b in edges:
            connect(a,b)
        # print(graph)
        
        return getParent(sou) == getParent(des)
        
            
            