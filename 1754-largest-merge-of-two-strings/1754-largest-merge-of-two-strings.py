class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        l1 = 0
        l2 = 0
        res = []
        
        while l1 < len(word1) and l2 < len(word2):
            
            if word1[l1] > word2[l2]:
                res.append(word1[l1])
                l1 += 1
            elif word2[l2] > word1[l1]:
                res.append(word2[l2])
                l2 += 1
            else:
                if word2[l2:] > word1[l1:]:
                    res.append(word2[l2])
                    l2 += 1
                else:
                    res.append(word1[l1])
                    l1 += 1
        if l1 < len(word1):
            res.append(word1[l1:])
        elif l2 < len(word2):
            res.append(word2[l2:])
        
        return "".join(res)
                    
                
        
                    
                    
                    
            
        