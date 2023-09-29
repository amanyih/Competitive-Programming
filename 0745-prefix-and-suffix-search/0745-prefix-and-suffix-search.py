class Node:
    
    def __init__(self):
        self.is_end = True
        self.children = {}
        self.indexes = set()
        
class Trie:
    
    def __init__(self):
        
        self.pref = Node()
        self.suffix = Node()
    
    def insert(self,word,index):
        node = self.pref
        
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
            node.indexes.add(index)
        node.is_end = True
        
        word = word[::-1]
        node = self.suffix
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            
            node = node.children[char]
            node.indexes.add(index)
        node.is_end = True
        
    def startsWith(self,word):
        node = self.pref
        
        for char in word:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.indexes
    def endsWith(self,word):
        word = word[::-1]
        node = self.suffix
        
        for char in word:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.indexes
        
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.memo = {}
        for i,word in enumerate(words):
            self.trie.insert(word,i)
        
    def f(self, pref: str, suff: str) -> int:
        trie = self.trie
        if (pref,suff) in self.memo:
            return self.memo[(pref,suff)]
        
        starts = trie.startsWith(pref)
        ends = trie.endsWith(suff)
        common = list(starts.intersection(ends))
        if len(common) == 0:
            self.memo[(pref,suff)] = -1
            return -1
        common.sort()
        self.memo[(pref,suff)] = common[-1]
        return common[-1]
        
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)