class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i,char in enumerate(word):
            val = ord(char) - 97
            if not node.children[val]:
                node.children[val] = TrieNode()
            if i == len(word) - 1:
                node.children[val].is_end = True
            node = node.children[val]

    def search(self, word: str) -> bool:
        node = self.root
        for i,char in enumerate(word):
            val = ord(char) - 97
            if node.children[val] and i == len(word)-1 and node.children[val].is_end:
                return True
            # print(node.children[val])
            if not node.children[val] or (i == len(word)-1 and not node.children[val].is_end):
                return False
            node = node.children[val]
        
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i,char in enumerate(prefix):
            val = ord(char) - 97
            if not node.children[val]:
                return False
            node = node.children[val]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)