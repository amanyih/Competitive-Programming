class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def dfs(cur,visited):
            
            visited.add(cur)
            
            row,col = cur
            
            for direction in directions:
                r,c = direction
                
                newR = row + r
                newC = col + c
                
                if 0 <= newR < len(board) and 0 <= newC < len(board[0]) and (newR,newC) not in visited and board[newR][newC] == "O":
                    dfs((newR,newC),visited)
        def check(sett):
            
            for cell in sett:
                r,c = cell
                
                if not (1 <= r < len(board)-1 and 1 <= c < len(board[0]) - 1):
                    return False
            return True
        def turn(sett):
            for cell in sett:
                r,c = cell
                board[r][c] = "X"
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if board[i][j] == "O":
                    visited = set()
                    dfs((i,j),visited)
                    if check(visited):
                        turn(visited)
                
        