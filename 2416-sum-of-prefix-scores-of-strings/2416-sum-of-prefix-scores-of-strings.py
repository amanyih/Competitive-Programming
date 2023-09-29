class Node:
    
    def __init__(self):
        self.pc = 0
        self.children = {}
        
class Trie:
    
    def __init__(self):
        
        self.root = Node()
    
    def insert(self,word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            
            node = node.children[char]
            node.pc += 1
    def search(self,word):
        
        node = self.root
        count = 0
        for char in word:
            count += node.children[char].pc
            node = node.children[char]
        
        return count
            

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = []
        for word in words:
            ans.append(trie.search(word))
        
        return ans
        