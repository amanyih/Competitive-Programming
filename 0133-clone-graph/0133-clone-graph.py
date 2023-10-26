"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        node_mapping = {}
        
        
        
        visited = set()
        q = deque([node])
        visited.add(node.val)
        
        while q:
            cur_node = q.popleft()
            # print(cur_node.val,"current node")
            if cur_node.val not in node_mapping:
                # print("creating",cur_node.val)
                node_mapping[cur_node.val] = Node(cur_node.val)
                
            copy_node = node_mapping[cur_node.val]
            
            for neig in cur_node.neighbors:
                if neig.val not in node_mapping:
                    node_mapping[neig.val] = Node(neig.val)
                copy_neig = node_mapping[neig.val]
                copy_node.neighbors.append(copy_neig)
                # print(neig.val)
                if neig.val not in visited:
                    q.append(neig)
                    visited.add(neig.val)
        # print(node_mapping[node.val])
        return node_mapping[node.val]
                    
        
        
        
        