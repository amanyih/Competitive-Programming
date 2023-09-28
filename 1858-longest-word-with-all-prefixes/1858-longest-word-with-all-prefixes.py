class Node:
    
    def __init__(self):
        self.is_end = False
        self.children = {}
    

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def allPrefixExist(self,word) -> bool:
        node = self.root
        
        for char in word:
            if char not in node.children or not node.children[char].is_end:
                return False
            node = node.children[char]
        return node.is_end

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        words.sort()
        ans = ""
        maxans = 0
        for word in words:
            if trie.allPrefixExist(word) and len(word) > maxans:
                maxans = len(word)
                ans = word
        return ans
        