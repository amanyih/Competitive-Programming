class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = set()
        
        def dfs(i):
            visited.add(i)
            
            for node in graph[i]:
                if node not in visited:
                    dfs(node)
        ans = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                ans += 1
        
        return ans
            
        