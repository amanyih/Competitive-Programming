class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length=len(board)
        board.reverse()
        def int_into_pos(square):
            length=len(board)
            r=(square-1)//length
            c=(square-1)%length
            if r%2:
                c=length-1-c
            return [r,c]
        def bfs(init):
            queue=deque([(init,0)])
            visited=set([init])
            while queue:
                square,step=queue.popleft()
                for i in range(1,7):
                    next_square=square+i
                    r,c=int_into_pos(next_square)
                    if board[r][c]!=-1:
                        next_square=board[r][c]
                    if next_square==len(board)**2:
                        return step+1
                    if next_square not in visited:
                        visited.add(next_square)
                        queue.append((next_square,step+1))
            return -1
        return bfs(1)