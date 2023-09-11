class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        groups = defaultdict(list)
        
        for i,group in enumerate(groupSizes):
            groups[group].append(i)
        
        ans = []
        
        for group in groups:
            if len(groups[group]) > group:
                for i in range(0,len(groups[group]),group):
                    ans.append(groups[group][:group])
            else:
                ans.append(groups[group])
        
        return ans
                
                
        