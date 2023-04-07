class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for road in roads:
            f,s = road
            graph[f].append(s)
            graph[s].append(f)
            
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                length = len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    length -= 1
                ans = max(ans,length)
        return ans
                
        