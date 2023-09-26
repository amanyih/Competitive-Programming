class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
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
            node = node.children[char]

    def search(self, word: str) -> bool:
        node = self.root
        for i,char in enumerate(word):
            if char in node.children and i == len(word)-1 and node.children[char].is_end:
                return True
            # print(node.children[val])
            if char not in node.children or (i == len(word)-1 and not node.children[char].is_end):
                return False
            node = node.children[char]
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i,char in enumerate(prefix):
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)