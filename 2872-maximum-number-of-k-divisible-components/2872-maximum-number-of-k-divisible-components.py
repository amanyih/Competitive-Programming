class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        
        graph = defaultdict(list)
        self.ans = 0
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node,visited = set()):

            visited.add(node)
            cur_sum = 0
            
            for nxt in graph[node]:
                if nxt not in visited:
                    cur_sum += dfs(nxt,visited)
            cur_sum += values[node]
            if cur_sum % k == 0:
                self.ans += 1
                return 0
            return cur_sum
        dfs(0)
        return self.ans
                
            