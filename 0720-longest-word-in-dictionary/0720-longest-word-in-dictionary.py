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
    
    def canBeBuiltOneAtATime(self,word):
        # print(word)
        node = self.root
        for char in word:
            if char not in node.children or not node.children[char].is_end:
                # print("False",word,char)
                return False
            node = node.children[char]
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        words.sort()
        ans = ""
        
        for word in words:
            # print(word)
            if trie.canBeBuiltOneAtATime(word) and len(word) > len(ans):
                ans = word
        return ans
        