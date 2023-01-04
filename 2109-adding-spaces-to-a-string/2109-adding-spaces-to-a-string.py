class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        container = []
        setSpace = set(spaces)
        n = len(s)
        
        for i in range(n):
            if i in setSpace:
                container.append(" ")
            container.append(s[i])
        
        return "".join(container)

        
        
        