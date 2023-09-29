class Node:
    
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.words = 0
class Trie:
    
    def __init__(self):
        
        self.root = Node()
    
    def insert(self,word):
        
        node = self.root
        
        for char in word:       
            if char not in node.children:
                node.children[char] = Node()
            
            node = node.children[char]
        node.words += 1
        node.is_end = True
    def count(self,word):
        node = self.root
        keys = list(node.children.keys())
        q = deque([])
        ans = 0
        
        for key in keys:
            index = word.find(key)
            if index >= 0:
                # print(key,index)
                q.append((index,node.children[key]))
                
        while q:
            start,node = q.popleft()
            ans += node.words
            keys = list(node.children.keys())
            for key in keys:
                index = word.find(key,start+1,len(word))
                if index >= 0:
                    q.append((index,node.children[key]))
        return ans
            
        


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.count(s)
        