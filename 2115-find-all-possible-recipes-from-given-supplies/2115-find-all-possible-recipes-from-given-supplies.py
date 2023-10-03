class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        n = len(recipes)
        allRecipes = set(recipes)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(n):
            ingredient = ingredients[i]
            recipe = recipes[i]
            for ingr in ingredient:
                graph[ingr].append(recipe)
                indegree[recipe] += 1
        q = deque(supplies)
        
        res = []
        
        while q:
            cur = q.popleft()
            
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                
                if indegree[nxt] == 0:
                    q.append(nxt)
                    if nxt in allRecipes:
                        res.append(nxt)
        return res
            
                
                
                
            