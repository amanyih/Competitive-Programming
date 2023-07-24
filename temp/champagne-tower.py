class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        
        before = {}
        
        
        def find(qr,qg):
            if (qr,qg) in before:
                x = before[(qr,qg)]
                return 0 if x <= 1 else x - 1
            
            if (qr,qg) == (0,0):
                before[(qr,qg)] = poured
                return poured - 1
            
            right = 0
            if qg <= qr-1:
                right = find(qr-1,qg) * 0.5
            left = 0
            
            if qg - 1 >= 0:
                left = find(qr-1,qg-1)* 0.5
            before[(qr,qg)] = right + left   
            if right + left >= 1:

                return right + left - 1
            return 0
        find(query_row,query_glass)
        x = before[(query_row,query_glass)]
        # print(before)
        return x if x <= 1 else 1
            