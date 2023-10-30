class Node:
    
    def __init__(self):     
        self.children ={}
        self.is_end = False
class Trie:
    
    def __init__(self):
        
        self.root = Node()
    
    def addWord(self,word):
        
        node = self.root
        
        for letter in word:
            
            if letter not in node.children:
                node.children[letter] = Node()
            
            node = node.children[letter]
        node.is_end = True
    def searchWord(self,word):
        
        node = self.root
        
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        
        return node.is_end
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)
        
        cache = {}
        
        def dp(index):
            if index in cache:
                return cache[index]
            if index == len(s):
                return True

            for i in range(index,len(s)):
                if trie.searchWord(s[index:i+1]):
                    if dp(i+1):
                        return True
            cache[index] = False
            return False
        
        return dp(0)
                
            
        
        
        