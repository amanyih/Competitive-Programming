class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = {}

        for match in matches:
            count[match[0]] = count.get(match[0],0) + 0
            count[match[1]] = count.get(match[1],0) + 1
        
        noLoss = []
        oneLoss = []
        for key in count:
            if count[key] == 0:
                noLoss.append(key)
            elif count[key] == 1:
                oneLoss.append(key)
        noLoss.sort()
        oneLoss.sort()
        return [noLoss,oneLoss]
