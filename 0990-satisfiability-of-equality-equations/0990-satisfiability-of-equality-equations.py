class UnionFind:
    def __init__(self, size):
        self.rank = defaultdict(int)
        self.rep = {i:i for i in range(size)}
        
    def representative(self, x):
        temp = x
        while self.rep[x] != x:
            x = self.rep[x]
        while self.rep[temp] != temp:
            self.rep[temp] = x
            temp = self.rep[temp]
        return x
		
    def union(self, x, y):
        xrep = self.rep[x]
        yrep = self.rep[y]
        if self.rank[xrep] >= self.rank[yrep]:
            self.rep[yrep] = xrep
            if self.rank[xrep] == self.rank[yrep]:
                self.rank[xrep] += 1
        else:
            self.rep[xrep] = yrep
                

    def connected(self, x, y):
        return self.rep[x] == self.rep[y]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = UnionFind(26)

        for equation in equations:
            a, b = equation[0], equation[-1]
            a = ord(a) - 97
            b = ord(b) - 97
            if equation[1] == "=":
                equal.union(a, b)

        for equation in equations:
            a, b = equation[0], equation[-1]
            a = ord(a) - 97
            b = ord(b) - 97
            if equation[1] == "!":
                if equal.connected(equal.representative(a), equal.representative(b)):
                    return False

        return True