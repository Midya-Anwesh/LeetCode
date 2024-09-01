# runtime = 43.0ms
# memory usage = 17.7MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root, target, nodes, curr_sum):
        if root is None:
            return
        if root.left is None and root.right is None:
            if curr_sum + root.val == target:
                yield (*nodes, root.val)
                return                
        nodes.append(root.val)
        yield from self.traverse(root.left, target, nodes, curr_sum+root.val)
        yield from self.traverse(root.right, target, nodes, curr_sum+root.val)
        nodes.pop(-1)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ret = []
        self.root = root
        if root is None:
            return []
        if (root.left is None) and (root.right is None) and (root.val == targetSum):
            yield [root.val]
        else:
            yield from self.traverse(root.left, targetSum, [root.val], root.val)
            yield from self.traverse(root.right, targetSum, [root.val], root.val)