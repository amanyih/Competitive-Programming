# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = defaultdict(list)
        
        def traverse(node):
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                traverse(node.left)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                traverse(node.right)
        
        traverse(root)
        
        q = deque([start])
        count = -1
        visited = set([start])
        
        while q:
            
            count += 1
            
            new_q = deque([])
            for el in q:
                for nxt in graph[el]:
                    if nxt not in visited:
                        visited.add(nxt)
                        new_q.append(nxt)
            
            q = new_q
        return count