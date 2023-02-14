class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        
        p = 0
        t = 0
        ans = 0
        
        while p < len(players) and t < len(trainers):
            if players[p] > trainers[t]:
                t += 1
            else:
                ans += 1
                t += 1
                p += 1
        
        return ans
            
            