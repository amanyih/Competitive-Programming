class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path + "/"
        stack = []
        
        cur = ""
        
        for char in path:
            
            if char == "/":
                
                if cur == "..":
                    
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += char
        
        path = "/" + "/".join(stack)
        
        return path
            
                
                
        