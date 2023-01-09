class Solution:
    def printVertically(self, s: str) -> List[str]:
        sLst = s.split()
        maxWidth = 0
        
        for word in sLst:
            maxWidth = max(maxWidth,len(word))
        container = [[] for _ in range(maxWidth)]
        
        for word in sLst:
            word = word + (" " * (maxWidth - len(word)))
            for i in range(len(word)):
                container[i].append(word[i])
        
        for j in range(len(container)):
            cur = container[j]
            
            while cur and cur[-1] == " ":
                cur.pop()
            container[j] = "".join(cur)
        return container
            

        