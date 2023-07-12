class Solution:
    def checkIfPrerequisite(self, num: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        
        for a,b in prerequisites:
            graph[a].append(b)
        
        dependencyGraph = defaultdict(set)
        isReachable = [[False for i in range(num)] for j in range(num)]
        
        
        for i in range(num):
            q = deque([i])
            
            while q:
                cur = q.pop()
                isReachable[i][cur] = True
                # print(i,cur)
                
                for n in graph[cur]:
                    if not isReachable[i][n]:
                        q.append(n)
        ans = []
        for a,b in queries:
            ans.append(isReachable[a][b])
        
        
            
            
            
            
            
        
        return ans
        