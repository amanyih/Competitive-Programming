class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        row,col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        visited = set()
        
        
        def countAdjBomb(row,col):
            count = 0
            for direction in directions:
                r,c = direction
                newR = row + r
                newC =col + c
                if 0 <= newR < len(board) and 0 <= newC < len(board[0]) and board[newR][newC] == "M":
                    count += 1
            return count
            
        def dfs(row,col):
            
            visited.add((row,col))
            count = countAdjBomb(row,col)
            if count != 0:
                board[row][col] = str(count)
            else:
                board[row][col] = "B"
                for direction in directions:
                    r,c = direction
                    newR = row + r
                    newC= col + c
                    
                    if 0 <= newR < len(board) and 0 <= newC < len(board[0]) and (newR,newC) not in visited and board[newR][newC] == "E":
                        dfs(newR,newC)
        dfs(row,col)
        return board
                    
            
            
            
            
            
        