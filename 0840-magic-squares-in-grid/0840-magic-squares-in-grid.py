class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        
        ans = 0
        for row in range(1,len(grid)-1):
            for col in range(1,len(grid[0])-1):
                top = grid[row-1][col-1] + grid[row-1][col]+grid[row-1][col+1]
                bottom = grid[row+1][col-1] + grid[row+1][col]+grid[row+1][col+1]
                middle= grid[row][col-1] + grid[row][col]+grid[row][col+1]
                left = grid[row-1][col-1] + grid[row][col-1]+grid[row+1][col-1]
                midd = grid[row-1][col] + grid[row][col]+grid[row+1][col]
                right= grid[row-1][col+1] + grid[row][col+1]+grid[row+1][col+1]
                lr = grid[row-1][col-1] + grid[row][col]+grid[row+1][col+1]
                rl =grid[row-1][col+1] + grid[row][col]+grid[row+1][col-1]
                
                st = set([grid[row-1][col-1],grid[row-1][col],grid[row-1][col+1],grid[row][col-1],grid[row][col],grid[row][col+1],grid[row+1][col-1],grid[row+1][col],grid[row+1][col+1]])
                if len(st) != 9:
                    continue
                flag = False
                for num in st:
                    if num > 9 or num < 1:
                        flag = True
                if flag:
                    continue
                    
                if top == bottom==middle==left==midd==right==lr==rl:
                    ans += 1
        return ans
                