# runtime = 27.0ms
# memory usage = 16.3MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, temp):
        if root is None:
            return
        elif root.left is None and root.right is None:
            yield temp+str(root.val)
            return
        yield from self.traverse(root.left, temp+str(root.val)+"->")
        yield from self.traverse(root.right, temp+str(root.val)+"->")

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ret = set()
        yield from self.traverse(root, "")