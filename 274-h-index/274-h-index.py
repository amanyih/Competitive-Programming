class Solution(object):
    def hIndex(self, citations):
        
        citations.sort()#nlogn
        
        for index,value in enumerate(citations):
            if len(citations) - index <= value:
                return len(citations) - index
        
        return 0
            
        