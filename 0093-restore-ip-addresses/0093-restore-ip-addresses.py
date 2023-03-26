class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        
        def backtrack(path,cur):
            # print(path,cur)
            if cur and len(path) == 3 and len(cur) == len(str(int(cur))) and 0<=int(cur)<= 255:
                path.append(cur)
                res.append(".".join(path))
                path.pop()
                return
            elif len(path) == 3 or cur == "":
                # print("he")
                return
            
            # print("forloop")
            for i in range(1,len(cur)+1):
                # print(cur[:i])
                
                if 0<=int(cur[:i])<= 255 and  len(cur[:i]) == len(str(int(cur[:i]))):
                    # print("onetrue")
                    path.append(cur[:i])
                    backtrack(path,cur[i:])
                    path.pop()
        backtrack([],s)
        
        return res
            
        