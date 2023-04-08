class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        visited = set()
        
        
        for row in range(len(isConnected)):
            for col in range(len(isConnected)):
                if isConnected[row][col] and row != col:
                    graph[row].append(col)
                    graph[col].append(row)
        
        def dfs(node):
            if node in visited:
                return 0
            
            visited.add(node)
            
            for n in graph[node]:
                dfs(n)
            return 1
        province = 0
        
        for city in range(len(isConnected)):
            province += dfs(city)
            # print("prov",province,"city",city)
        return province
        