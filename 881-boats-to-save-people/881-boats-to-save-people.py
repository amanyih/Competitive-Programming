class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low = 0
        high = len(people) -1
        
        boats = 0
        
        while low < high:
            if people[low] + people[high] > limit:
                high -=1
            else:
                high -= 1
                low += 1
            
            boats += 1
        
        return boats +1 if low == high else boats