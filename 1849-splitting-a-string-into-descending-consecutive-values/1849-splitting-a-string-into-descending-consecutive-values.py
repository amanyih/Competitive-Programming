class Solution:
    def splitString(self, s: str) -> bool:
        
        def search(path,curState):
            
            if path and path[-1] -int(curState) == 1:
                return True
            elif len(curState) == 1:
                return False
            
            for i in range(1,len(curState)):
                if not path:
                    path.append(int(curState[:i]))
                    if search(path,curState[i:]):
                        return True
                    path.pop()
                elif path[-1] - int(curState[:i]) == 1:
                    path.append(int(curState[:i]))
                    if search(path,curState[i:]):
                        return True
                    path.pop()
            return False
        
        return search([],s)
                    
                
            