class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        
        ans = [1]*n
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def merge(dict1,dict2):
            # print("-------------")
            # print(dict1,dict2)
            
            for key in dict2:
                if key in dict1:
                    dict1[key] += dict2[key]
                else:
                    dict1[key] = dict2[key]
            # print(dict1)
            return dict1
                
            
        
        def dfs(node,parent = None):
            nonlocal labels
            counts = []
            
            for neig in graph[node]:
                if parent != neig:
                    counts.append(dfs(neig,node))
            
            
            dict1 = {labels[node]:1}
            
            for count in counts:
                dict1 = merge(dict1,count)
            # print(node,counts,dict1)
            ans[node] = dict1[labels[node]]
            return dict1
        dfs(0)
        return ans
            
            
                
        
        
        