class Node:
    
    def __init__(self):
        
        self.is_end = False
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
        node.is_end = True
    def search(self,word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        res = []
        
        def backtrack(i = 0,cur= []):
            # print(i,cur)
            if i == len(s):
                res.append(cur[:])
                return
            
            for j in range(i,len(s)):
                word = s[i:j+1]
                # print(word,i,j )
                if trie.search(word):
                    cur.append(word)
                    backtrack(j+1,cur)
                    cur.pop()
        backtrack()
        
        for i in range(len(res)):
            res[i] = " ".join(res[i])
        
        return res
                    
                    
                
            
            
            
            
        