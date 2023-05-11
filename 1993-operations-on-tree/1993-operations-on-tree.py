class LockingTree:

    def __init__(self, parent: List[int]):
        
        self.graph = defaultdict(list)
        self.locked = defaultdict(int)
        self.ancestors = defaultdict(set)
        self.desc = defaultdict(set)
        
        for i,p in enumerate(parent):
            self.graph[p].append(i)
            
        def dfs(node,par):
            self.ancestors[node].update(par)
            
            newParents = par.union(set([node]))
            for n in self.graph[node]:
                dfs(n,newParents)
        def children(node):
            
            childs = set()
            for c in self.graph[node]:
                childs.update(children(c))
            
            self.desc[node] = childs
            
            return childs.union(set([node]))
        dfs(0,set())
        children(0)
            
    def lock(self, num: int, user: int) -> bool:
        
        if self.locked[num]:
            return False
        
        self.locked[num] = user
        return True
        
    def unlock(self, num: int, user: int) -> bool:
        
        if self.locked and self.locked[num] == user:
            self.locked[num] = 0
            return True
        return False
    
    def upgrade(self, num: int, user: int) -> bool:
        
        if self.locked[num]: return False
        
        for node in self.ancestors[num]:
            if self.locked[node]: return False
        
        count = 0
        for node in self.desc[num]:
            if self.locked[node]:
                self.locked[node] = 0
                count += 1
        if not count:
            return False
        
        self.locked[num] = user
        return True
            
        
            
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)