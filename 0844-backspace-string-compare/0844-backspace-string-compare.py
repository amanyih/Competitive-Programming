class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        astack = []
        bstack = []
        
        for char in s:
            if char == "#" and astack:
                astack.pop()
            elif char != "#":
                astack.append(char)
        for char in t:
            if char == "#" and bstack:
                bstack.pop()
            elif char != "#":
                bstack.append(char)
        
        return "".join(astack) == "".join(bstack)
        
        