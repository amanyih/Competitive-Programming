class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()
        
        def dfs(sr,sc,color,orColor):
            
            
            if image[sr][sc] == orColor:
                image[sr][sc] = color
                for direction in directions:
                    r,c = direction
                    if 0 <= sr + r < len(image) and 0 <= sc + c < len(image[0]) and (sr+r,sc+c) not in visited:
                        visited.add((sr+r,sc+c))
                        dfs(sr+r,sc+c,color,orColor)
        dfs(sr,sc,color,image[sr][sc])
        return image