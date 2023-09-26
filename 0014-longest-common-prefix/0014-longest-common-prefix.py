class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.count = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i,char in enumerate(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            if i == len(word) - 1:
                node.children[char].is_end = True
            node.count += 1
            node = node.children[char]
    def findCommon(self,count):
        common = []
        node = self.root
        while len(node.children) == 1:
            key = list(node.children.keys())[0]
            if node.count == count:
                common.append(key)
            node = node.children[key]
        return "".join(common)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        
        for word in strs:
            trie.insert(word)
        
        return trie.findCommon(len(strs))
        
        