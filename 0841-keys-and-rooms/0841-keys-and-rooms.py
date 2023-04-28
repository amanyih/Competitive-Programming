class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        
        keys = set()
        keys.add(0)
        q = deque(rooms[0])
        
        while q:
            # print(q)
            cur = q.popleft()
            keys.add(cur)
            
            for key in rooms[cur]:
                if key not in keys:
                    q.append(key)
        return len(keys) == len(rooms)
        