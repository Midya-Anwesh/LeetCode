# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subTreeSum = dict()
        def dfs(node: Optional[TreeNode], level: int) -> int:
            if node is None:
                return 0
            subTreeSum[node] = dfs(node.left, level+1) + dfs(node.right, level+1) + node.val
            return subTreeSum[node]
        totalSum = dfs(root, 0)

        def makeCut(node: Optional[TreeNode], level: int) -> int:
            ret = -float('inf')
            # Cut left if left exists
            if node.left:
                ret = max(ret, (totalSum - subTreeSum[node.left]) * subTreeSum[node.left] )
                # Recursively do it to the left subtree
                ret = max(ret, makeCut(node.left, level+1))
            # Cut right if right exists
            if node.right:
                ret = max(ret, (totalSum - subTreeSum[node.right]) * subTreeSum[node.right] )
                # Recursively do it to the right subtree
                ret = max(ret, makeCut(node.right, level+1))
            return ret
        
        return makeCut(root, 0) % 1_000_000_007