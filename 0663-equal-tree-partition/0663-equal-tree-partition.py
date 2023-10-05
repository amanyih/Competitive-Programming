# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def calculate_sum(root):
            if not root:
                return 0
            left_val = calculate_sum(root.left)
            right_val = calculate_sum(root.right)
            return left_val + right_val + root.val

        total_sum = calculate_sum(root)
        def can_be_partitioned(root):
            if root == None:
                return [False,0]

            found_in_left,left_val = can_be_partitioned(root.left)
            found_in_right,right_val = can_be_partitioned(root.right)
            cur_val = left_val + right_val + root.val

            if found_in_left or found_in_right:
                return [True,cur_val]

            if ( root.left and total_sum - left_val  == left_val) or ( root.right and total_sum -right_val == right_val):
                return [True,cur_val]

            return [False,cur_val]
        return can_be_partitioned(root)[0]
        