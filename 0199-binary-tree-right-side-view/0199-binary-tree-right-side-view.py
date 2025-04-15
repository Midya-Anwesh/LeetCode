# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If there is no node return empty array
        if root is None:
            return []
        # Otherwise we know first level is 0
        # Check for max Level
        initLevel, maxLevel = 0, 0
        # map to store nodes level wise
        levelWiseRightNodes = dict()
        # We will use in-order traversal as
        # It goes to right most node of that level as last as possible
        def traverse(root: Optional[TreeNode], level: int) -> None:
            nonlocal maxLevel
            # Base case
            if root is None:
                return
            # As we traverse rightmost node of a level as late as possible
            # So, store current node against current level
            levelWiseRightNodes[level] = root.val
            # Update max level properly
            maxLevel = max(maxLevel, level)
            # Check nodes of next level
            traverse(root.left, level+1)
            traverse(root.right, level+1)
        traverse(root, 0)
        # We know start and end level of the tree, traverse start to end and
        # Store the rightmost node of a level in the array to be returned
        return [levelWiseRightNodes[level] for level in range(initLevel, maxLevel+1)]