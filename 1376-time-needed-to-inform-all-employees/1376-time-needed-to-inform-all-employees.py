class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        
        for head,sub in enumerate(manager):
            graph[sub].append(head)
        
        visited = set()
        
        ans = 0
        
        def dfs(cur,level):
            # print(cur,informTime[cur])
            nonlocal ans
            
            visited.add(cur)
            ans = max(ans,level)
            for n in graph[cur]:
                if n not in visited:
                    dfs(n,level+informTime[n])
        
        dfs(headID,informTime[headID])
        return ans
            
            
            