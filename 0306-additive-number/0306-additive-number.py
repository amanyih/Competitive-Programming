class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        
        
        def find(path,curState):
            # print(path,curState)
            if len(path) >= 2 and path[-2] + path[-1] == int(curState) and len(curState) == len(str(int(curState))):
                return True
            elif len(curState) == 1:
                return False
            
            for i in range(1,len(curState)):
                if len(path) < 2:
                    path.append(int(curState[:i]))
                    if len(curState[:i]) == len(str(int(curState[:i]))) and  find(path,curState[i:]):
                        return True
                    path.pop()
                    
                elif path[-2] + path[-1] == int(curState[:i]):
                    path.append(int(curState[:i]))
                    if len(curState[:i]) == len(str(int(curState[:i]))) and  find(path,curState[i:]):
                        return True
                    path.pop()
            
            return False
        return find([],num)
            
                    