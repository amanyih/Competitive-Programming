class Solution:
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        
        for i in range(len(g)):
            graph[i] = g[i]
        
        ans = []
        def dfs(source,target,path=[]):
            path.append(source)
            
            if source == target:
                ans.append(path[:])
            
            for n in graph[source]:
                dfs(n,target,path)
            
            path.pop()
        dfs(0,len(g)-1)
 
        return ans
            
        
        
        