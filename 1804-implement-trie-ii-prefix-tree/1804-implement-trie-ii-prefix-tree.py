class Node:
    
    def __init__(self):
        self.sw = 0
        self.ew = 0
        self.children = {}
        
class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node.children[char].sw += 1
            node = node.children[char]
        
        node.ew += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.ew
        

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.sw
        
    def erase(self, word: str) -> None:
        node = self.root
        
        for char in word:
            node.children[char].sw -= 1
            node = node.children[char]
        
        node.ew -= 1
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)