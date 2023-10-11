class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        def turnLeft(direction):
            if direction == (0,1):
                return (-1,0)
            if direction == (1,0):
                return (0,1)
            if direction == (0,-1):
                return (1,0)
            if direction == (-1,0):
                return (0,-1)
        def turnRight(direction):
            if direction == (0,1):
                return (1,0)
            if direction == (1,0):
                return (0,-1)
            if direction == (0,-1):
                return (-1,0)
            if direction == (-1,0):
                return (0,1)
            
        
        direction = (-1,0)
        current = (0,0)
        for inst in instructions:
            if inst == "L":
                direction = turnLeft(direction)
            elif inst == "R":
                direction = turnRight(direction)
            else:
                x,y = direction
                px,py = current
                current = (x+px,py+y)
        
        return current == (0,0) or direction != (-1,0)
            
                
                
        
        