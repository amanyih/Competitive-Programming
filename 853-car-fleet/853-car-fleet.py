class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedLocation = {}
        stack = []

        for i in range(len(position)):
            speedLocation[position[i]] = i
        
        position.sort(reverse= True)

        for pos in position:
            time = (target - pos)/speed[speedLocation[pos]]
            if stack:
                if time>stack[-1][-1]:
                    stack.append([pos,time])
            else:
                stack.append([pos,time])
        
        return len(stack)
        
        