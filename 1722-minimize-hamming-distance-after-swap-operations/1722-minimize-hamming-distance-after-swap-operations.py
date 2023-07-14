class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
   
        graph = defaultdict(list)
        visited = set()
        
        for a,b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node,v):
            
            visited.add(node)
            v.add(node)
            
            for n in graph[node]:
                if n not in visited:
                    dfs(n,v)
            
        
        components = []
        
        for i in range(len(source)):
            if i not in visited:
                s = set()
                dfs(i,s)
                components.append(s)
        ans = 0
        for component in components:
            a = []
            for c in component:
                a.append(source[c])
            aCount = Counter(a)
            
            for c in component:
                
                if target[c] in aCount:
                    aCount[target[c]] -= 1
                    if aCount[target[c]] == 0:
                        del aCount[target[c]]
                else:
                    ans += 1
        
        return ans
                
        
        
            
        
        
        