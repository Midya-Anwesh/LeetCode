# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxDepth, deepestNodes, parent = -1, set(), dict()

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            nonlocal maxDepth, deepestNodes
            if node is None:
                return
            if depth > maxDepth:
                deepestNodes = set([node])
                maxDepth = depth
            elif depth == maxDepth:
                deepestNodes.add(node)
            if node.left:
                parent[node.left] = node
                dfs(node.left, depth+1)
            if node.right:
                parent[node.right] = node
                dfs(node.right, depth+1)
        dfs(root, 0)

        while len(deepestNodes) > 1:
            nextNodes = set()
            for node in deepestNodes:
                nextNodes.add(parent[node])
            deepestNodes = nextNodes
        return deepestNodes.pop()