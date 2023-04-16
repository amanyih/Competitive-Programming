class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()
        
        def backtrack(path,curSum,target):
            if curSum == target:
                x = path[:]
                x.sort()
                res.add(tuple(x))
                return
            elif curSum > target:
                return
            
            for candidate in candidates:
                if curSum + candidate <= target:
                    path.append(candidate)
                    backtrack(path,curSum+candidate,target)
                    path.pop()
        backtrack([],0,target)
        return [list(x) for x in res]
                
        