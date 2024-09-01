# runtime = 50.0ms
# memory usage = 17.8MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_all_string(self, root: Optional[TreeNode], temp: str):
        if root is None:
            return
        elif root.left is None and root.right is None:
            self.strings.add("".join(reversed(temp+chr(root.val+97))))
            return
        self.get_all_string(root.left, temp+chr(root.val+97))
        self.get_all_string(root.right, temp+chr(root.val+97))

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.strings = set()
        self.get_all_string(root, "")
        print(self.strings)
        return sorted(self.strings)[0]