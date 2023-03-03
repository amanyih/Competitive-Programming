class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        anss = 0
        def doBinarySearch(target):
            left = 0
            right = len(heaters) - 1
            mid = (left + right ) // 2
            ans = abs(target - heaters[mid])
            while left <= right:
                mid = (left + right) // 2
                ans = min(ans,abs(target-heaters[mid]))
                
                if heaters[mid] < target:
                    
                    left = mid + 1
                elif heaters[mid] > target:
                    right = mid -1
                else:
                    return 0
            return ans
        
        for house in houses:
            anss = max(anss,doBinarySearch(house))
        
        return anss
            
            
        