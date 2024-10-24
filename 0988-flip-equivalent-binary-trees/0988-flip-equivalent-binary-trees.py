# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None:
            return root2 is None
        elif root2 is None:
            return root1 is None

        def isEquiv(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
            if r1 is None and r2 is None:
                return True
            elif r1 is None or r2 is None:
                return False
            elif r1.val != r2.val:
                return False
            return (isEquiv(r1.left, r2.left) or isEquiv(r1.left, r2.right)) and\
            (isEquiv(r1.right, r2.right) or isEquiv(r1.right, r2.left))

        return isEquiv(root1, root2)