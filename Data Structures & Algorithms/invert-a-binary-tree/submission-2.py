# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        leftSubTree = self.invertTree(root.left)
        rightSubTree = self.invertTree(root.right)
        root.left, root.right = rightSubTree, leftSubTree
        return root