class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        
        
        occurrence = {}
        
        for i,char in enumerate(s):
            occurrence[char] = i
        stack = []
        seen = set()
        
        for i,char in enumerate(s):
            
            if char not in seen:
                while stack and stack[-1] > char and occurrence[stack[-1]] > i:
                    poped = stack.pop()
                    seen.remove(poped)
                stack.append(char)
                seen.add(char)
        
        return "".join(stack)
            
            