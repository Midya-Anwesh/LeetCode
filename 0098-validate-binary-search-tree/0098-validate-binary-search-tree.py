# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(root: Optional[TreeNode]) -> List[int]:
            nonlocal ans
            if root.left is None and root.right is None:
                return [root.val, root.val]
            if root.left is None:
                left_sub_tree = [root.val, root.val]
                right_sub_tree = dfs(root.right)
                ans &= min(right_sub_tree) > root.val
            elif root.right is None:
                right_sub_tree = [root.val, root.val]
                left_sub_tree = dfs(root.left)
                ans &= max(left_sub_tree) < root.val
            else:
                left_sub_tree = dfs(root.left)
                right_sub_tree = dfs(root.right)
                ans &= max(left_sub_tree) < root.val < min(right_sub_tree)
            all_val = [*left_sub_tree, *right_sub_tree, root.val]
            return [max(all_val), min(all_val)]
        dfs(root)

        return ans
