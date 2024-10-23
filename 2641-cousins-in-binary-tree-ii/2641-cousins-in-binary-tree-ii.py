# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = dict()
        def dfs(root: Optional[TreeNode], level: int) -> None:
            if root is None:
                return
            level_sum[level] = level_sum.get(level, 0)+root.val
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)

        def normalize_childs(root: Optional[TreeNode], level: int) -> None:
            if (root is None): # or (root.left is None and root.right is None):
                return
            sibling_sum = 0
            if root.left is not None:
                sibling_sum += root.left.val
            if root.right is not None:
                sibling_sum += root.right.val
            if root.left is not None:
                root.left.val = level_sum[level+1]-sibling_sum
            if root.right is not None:
                root.right.val = level_sum[level+1]-sibling_sum
            normalize_childs(root.left, level+1)
            normalize_childs(root.right, level+1)
        normalize_childs(root, 0)
    
        root.val = 0

        return root