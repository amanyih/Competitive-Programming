class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        cache = {}
        
        def findLastStone(index,added,subtracted):
            if (index,added,subtracted) in cache:
                return cache[(index,added,subtracted)]
            if index < 0:
                return abs(added-subtracted)
            
            sub = findLastStone(index-1,added,subtracted+stones[index])
            add = findLastStone(index-1,added+stones[index],subtracted)
            
            cur = min(sub,add)
            cache[(index,added,subtracted)] = cur
            return cur
        return findLastStone(len(stones)-1,0,0)
        