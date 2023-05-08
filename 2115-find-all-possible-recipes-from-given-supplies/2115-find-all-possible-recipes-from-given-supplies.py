class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        
        
        graph = defaultdict(list)
        inde = defaultdict(int)
        
        
        for i in range(len(recipes)):
            
            
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
            inde[recipes[i]] += len(ingredients[i])
        
        q = deque(supplies)
        rec = set(recipes)
        
        res = []
        
        while q:
            cur = q.popleft()
            
            if cur in rec:
                res.append(cur)
            
            for c in graph[cur]:
                inde[c] -= 1
                if inde[c] ==0:
                    q.append(c)
        
        return res