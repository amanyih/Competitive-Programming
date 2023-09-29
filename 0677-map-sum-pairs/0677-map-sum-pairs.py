class Node:
    
    def __init__(self):
        self.children = {}
        self.prefvalue = 0
        self.wordvalue = 0
        self.is_end = False

class MapSum:

    def __init__(self):
        self.root = Node()
        
    def insert(self, key: str, val: int) -> None:
        node = self.root
        sub = self.search(key)
        
        for char in key:
            if char not in node.children:
                node.children[char] = Node()
            node.children[char].prefvalue += (val-sub)
            node = node.children[char]
        node.wordvalue = val
        node.is_end = True

    def sum(self, prefix: str) -> int:
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefvalue
        
    
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        if node.is_end:
            return node.wordvalue
        return 0
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)