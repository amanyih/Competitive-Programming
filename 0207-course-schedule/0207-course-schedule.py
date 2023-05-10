class Solution:
    def canFinish(self, num: int, preq: List[List[int]]) -> bool:
        
        # print("num",num)
        
        
        graph = defaultdict(list)
        
        for pre in preq:
            a,b = pre
            graph[b].append(a)
        black = set()
        
        
        def dfs(node,grey):
            grey.add(node)
            
            # print(node,grey)
            
            for g in graph[node]:
                if g not in black and g in grey:
                    return False
                elif g not in black:
                    if not dfs(g,grey):
                        return False
            black.add(node)
            return True
        
        for i in range(num):
            # print("i",i)
            grey = set()
            if i not in black and not dfs(i,grey):
                return False
        
        return True