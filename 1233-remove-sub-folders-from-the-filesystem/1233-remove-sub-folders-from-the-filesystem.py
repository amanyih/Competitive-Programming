class Node:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    
    def __init__(self):
        self.root = Node()
    
    def addFolder(self,folder):
        node = self.root
        
        for char in folder:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.isEnd = True
    def removeSubFolders(self):
        node = self.root
        res = []
        
        q = deque([(node,[])])
        
        while q:
            cur,path = q.popleft()
            
            for char in cur.children:
                cur_path = path + [char]
                if cur.children[char].isEnd and "/" in cur.children[char].children:
                    res.append(cur_path)
                else:
                    if cur.children[char].isEnd:
                        res.append(cur_path)
                    q.append((cur.children[char],cur_path))
        for i in range(len(res)):
            res[i] = "".join(res[i])
        return res
            
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.addFolder(f)
        return trie.removeSubFolders()
        