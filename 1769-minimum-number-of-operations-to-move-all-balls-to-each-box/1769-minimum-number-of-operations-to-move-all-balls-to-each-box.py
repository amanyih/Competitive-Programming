class Solution:
    def minOperations(self, boxes: str) -> List[int]:
          
        after = 0
        a = 0
        before = 0
        b= 0
        
        for i,box in enumerate(boxes):
            
            if box == "1":
                after += i
                a += 1
        ans = []
        
        for i, box in enumerate(boxes):
            n = len(boxes)-1-i
            if box == "1":
                after -= i
                a -= 1
            moves = (after - (i*a)) + (before - ((n)*b))
            ans.append(moves)
            if box == "1":
                before += n
                b += 1
        return ans
                
                
                                                                                                                                                                                                                                                                                                                                                                                                               