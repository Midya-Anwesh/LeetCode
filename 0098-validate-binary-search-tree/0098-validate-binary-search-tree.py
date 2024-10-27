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
            # If it is a leaf Node, max node and min node that can be reached is the current node itself
            if root.left is None and root.right is None:
                return [root.val, root.val]

            # If current node doesn't have a left child / sub tree
            if root.left is None:
                # Max and Min value nodes from left sub tree are the current node itself
                left_sub_tree = [root.val, root.val]
                # Get max and min value that are present in right sub tree
                right_sub_tree = dfs(root.right)
                # As the node doesn't have left sub tree it will hold bst iff 
                # Min value available in right sub tree is greater than current root val
                ans &= min(right_sub_tree) > root.val

            # If current node doesn't have a right child / sub tree
            elif root.right is None:
                # Max and Min value node from right sub tree are the current node itself
                right_sub_tree = [root.val, root.val]
                # Get max and min value that are present in left sub tree
                left_sub_tree = dfs(root.left)
                # Condition for bst will hold iff max value of left sub tree is less than current node value
                ans &= max(left_sub_tree) < root.val

            # If current node have both left and right child / sub tree
            else:
                # Get max and min value from left sub tree
                left_sub_tree = dfs(root.left)
                # Get max and min value from right sub tree
                right_sub_tree = dfs(root.right)
                # Condition for bst will hold iff
                # Max of left sub tree is less than value of current node and 
                # Min of right sub tree is greater than value of current node
                ans &= max(left_sub_tree) < root.val < min(right_sub_tree)
            
            # Creating an array of all possible max and min value that can be reached by current node
            all_val = [*left_sub_tree, *right_sub_tree, root.val]
            # Return max value and min value that can be reached from the current node
            return [max(all_val), min(all_val)]
        dfs(root)

        return ans
