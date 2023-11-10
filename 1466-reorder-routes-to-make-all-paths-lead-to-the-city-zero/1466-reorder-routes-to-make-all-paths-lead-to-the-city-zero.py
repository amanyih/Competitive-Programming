class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        reverse = defaultdict(set)
        
        for a,b in connections:
            graph[a].add(b)
            reverse[b].add(a)
        
        stack = [0]
        ans = 0
        visited = set()
        
        while stack:
            
            cur = stack.pop()
            visited.add(cur)
            
            for nxt in graph[cur]:
                if nxt not in visited:
                    stack.append(nxt)
                    ans += 1
            for nxt in reverse[cur]:
                if nxt not in visited:
                    stack.append(nxt)
        
        return ans
        