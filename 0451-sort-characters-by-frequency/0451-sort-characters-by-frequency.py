class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        arr = []
        
        for key in count:
            arr.append((key,count[key]))
        
        arr.sort(key = lambda x : -x[1])
        
        res = []
        
        for char,count in arr:
            res.append(char * count )
        
        return "".join(res)
            
        