class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefixSum = [0]
        for t in travel:
            prefixSum.append(prefixSum[-1]+t)
        
        trackLocation = {"G" : 0, "P":0,"M":0}
        totalTime = 0
        for index in range(len(garbage)):
            for trash in garbage[index]:
                cur = prefixSum[index]
                last = prefixSum[trackLocation[trash]]
                
                totalTime += cur - last + 1
                
                trackLocation[trash] = index
        
        return totalTime
                
                
                
        
        