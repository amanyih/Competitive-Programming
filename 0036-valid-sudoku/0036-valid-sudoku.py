class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = [defaultdict(int) for i in range (9)]
        rows = [defaultdict(int) for i in range(9)]
        subBoxes = [defaultdict(int) for i in range(9)]
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".": continue
                cols[col][board[row][col]] += 1
                rows[row][board[row][col]] += 1
                
                curBoxRow = (row // 3)
                curBoxCol = (col // 3)
                
                if curBoxRow == 0:
                    curBoxCol += 0
                else:
                    curBoxCol += 3 if curBoxRow == 1 else 6
                subBoxes[curBoxCol][board[row][col]] += 1
                
                if cols[col][board[row][col]] > 1 or rows[row][board[row][col]] > 1 or subBoxes[curBoxCol][board[row][col]] > 1:
                    print(row,col,board[row][col])
                    return False
        
        return True
                
                
        