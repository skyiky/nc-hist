# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def dfs(node):
            nonlocal d
            if not node:
                return 0
            l_subtree_height = dfs(node.left)
            r_subtree_height = dfs(node.right)
            local_d = l_subtree_height + r_subtree_height
            d = max(d, local_d)
            return 1 + max(l_subtree_height, r_subtree_height)

        dfs(root)
        return d
