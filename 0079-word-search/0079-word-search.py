class Solution:
    
    """
    ["A","B","C","E"]
    ["S","F","E","S"]
    ["A","D","E","E"]
    ABCESEEEFS
    
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def isValid(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def backtrack(row,col,index,visited):
            # print(row,col,index,visited)
            
            if index  == len(word):
                return True
            if board[row][col] != word[index]:
                return False
            if index + 1 == len(word):
                return True

            visited.add((row,col))
            
            for r,c in directions:
                new_r,new_c = row+r,col+c
                
                if (new_r,new_c) not in visited and isValid(new_r,new_c):
                    if backtrack(new_r,new_c,index+1,visited):
                        return True
            visited.remove((row,col))
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r,c,0,set()):
                    return True
        return False
        