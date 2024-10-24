# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ans will hold ans
        ans = -float('inf')
        def get_len(root: Optional[TreeNode]) -> int:
            # If root is None then height of it's parent is 0
            if root is None:
                return 0
            nonlocal ans
            # Recursively calculate left and right height
            left_height = get_len(root.left)        
            right_height = get_len(root.right)
            # Calculate diameter and check if it's greater than current max
            ans = max(ans, left_height+right_height)

            # This step is treaky
            # For a parent only thing matter is maximum of left height and right height of child
            # Maximum of left and right height matter because for a parent it's left height might be
            # maximized by picking left height of imidiate left child and then picking right height of it's child
            # For parent the height will be incremented by 1
            # [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
            # Use it for a dry-run to grasp the logic
            return max(left_height + 1, right_height + 1)
        get_len(root)
        return ans