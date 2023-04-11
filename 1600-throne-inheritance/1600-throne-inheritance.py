class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.order = defaultdict(list)
        self.order[kingName] = []
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.order[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        cur = []
        
        visited = set()
        
        def find(curRuler):
            
            if curRuler not in self.dead:
                cur.append(curRuler)
            visited.add(curRuler)
            
            for child in self.order[curRuler]:
                find(child)
        find(self.king)
        return cur
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()