class Node:
    
    def __init__(self):
        
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        q = deque([self.root])
        
        for index,char in enumerate(word):
            new_q = deque([])
            while q:
                if char == ".":
                    for node in q:
                        new_q.extend(list(node.children.values()))
                else:
                    found = False
                    for node in q:
                        if char in node.children:
                            found = True
                            new_q.append(node.children[char])
                    if not found:
                        return False
                q = []
            q = new_q
        found = False
        for node in q:
            if node.is_end:
                found = True
        return found
            
            
                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)