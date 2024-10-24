# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rev_odd(self, root: Optional[TreeNode], level: int, level_values: dict[int:List[int]]) -> None:
        if root is None:
            return
        elif level&1:
            root.val = level_values[level].pop(-1)
        self.rev_odd(root.left, level+1, level_values)
        self.rev_odd(root.right, level+1, level_values)

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        level_values = dict()
        def dfs(root: Optional[TreeNode], level: int) -> None:
            if root is None:
                return
            elif level&1:
                if not level in level_values:
                    level_values[level] = [root.val]
                else:
                    level_values[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        
        self.rev_odd(root, 0, level_values)

        return root