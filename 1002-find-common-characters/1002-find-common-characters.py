class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
          {b: [1,2]}
        ["bella","label","roller"]
        
        """
        
        ref = Counter(words[0])
        
        for i in range(1,len(words)):
            new = Counter(words[i])
            
            for key in ref:
                ref[key] = min(ref[key],new[key])
        
        ans = []
        
        for key in ref:
            
            for j in range(ref[key]):
                ans.append(key)
        return ans
            
                
            
            