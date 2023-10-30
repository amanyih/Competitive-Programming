class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        char_map = {}
        
        stack = []
        
        
        for i,char in enumerate(s):
            if char == "(":
                stack.append(i)
                char_map[i] = char
            elif char == ")":
                if stack:
                    j = stack.pop()
                    char_map[i] = char
                else:
                    char_map[i] = ""
            else:
                char_map[i] = char
        
        while stack:
            j = stack.pop()
            char_map[j] = ""
        
        return "".join([char_map[i] for i in range(len(s))])
            
        