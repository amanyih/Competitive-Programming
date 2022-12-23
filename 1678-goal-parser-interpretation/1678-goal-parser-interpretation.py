class Solution:
    def interpret(self, command: str) -> str:
        
        left = 0
        res = ""
        
        while left < len(command):
            if command[left] == "G":
                res += "G"
                left += 1
            elif command[left] == "(" and command[left+1] == "a":
                res += "al"
                left += 4
            else:
                res += "o"
                left += 2
        
        return res
            