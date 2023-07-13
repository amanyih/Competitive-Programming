class UnionFind:
    def __init__(self, size):
        self.root = {i: i for i in range(size)}
        self.rank = [0] * size
        self.size = size

    def find(self, member):
        root = member
        while root != self.root[root]:
            root = self.root[root]

        while member != root:
            parent = self.root[member]
            self.root[member] = root
            member = parent

        return root

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.root[x] == self.root[y]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        acc = {}
        uf = UnionFind(len(accounts))
        
        for j in range(len(accounts)):
            
            for i in range(1,len(accounts[j])):
                account = accounts[j][i]
                if account in acc:
                    uf.union(acc[account],j)
                    # print("once")
                    # print(account)
                else:
                    acc[account] = j
        
        # print(acc)
        merged = {}
        for i in range(len(accounts)):
            parent = uf.find(i)
            
            if parent == i:
                merged[i] = accounts[i][1:]
        
        for i in range(len(accounts)):
            parent = uf.find(i)
            
            if parent != i:
                merged[parent].extend(accounts[i][1:])
        # print(merged)
        ans = []
        for key in merged:
            x =list( set( merged[key]))
            x.sort()
            ans.append([accounts[key][0]] + x)
        
        return ans
        
                
        
        
        
        