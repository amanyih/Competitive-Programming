class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        pathCollection = defaultdict(list)
        
        for path in paths:
            
            path = path.split()
            directory = path[0]
            
            for i in range(1,len(path)):
                curFile = path[i]
                content = []
                pointer = len(curFile) - 2
                
                while pointer >= 0 and curFile[pointer] != "(":
                    content.append(curFile[pointer])
                    pointer -= 1
                content = "".join(content)
                pathCollection[content].append(directory+"/"+curFile[:pointer])
        
        ans = []
        
        for file in pathCollection:
            if len(pathCollection[file]) > 1:
                ans.append(pathCollection[file])
        
        return ans
        
            
        