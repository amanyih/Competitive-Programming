class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        
        def find(num):
            left = 0
            right = len(potions)
            
            while left < right:
                mid = (left + right) // 2
                if potions[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left
        ans = []
        
        for spell in spells:
            ans.append(len(potions) - find(ceil(success/spell)))
        return ans
            