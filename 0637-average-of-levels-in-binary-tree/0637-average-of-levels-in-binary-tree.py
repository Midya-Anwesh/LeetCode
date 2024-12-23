from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sumAndCount = defaultdict(lambda:[0, 0]) # sumAndCount[level] = [sum, count] for each level
        def dfs(root: Optional[TreeNode], level: int) -> None:
            if root is None:
                return
            sumAndCount[level][0] += root.val
            sumAndCount[level][1] += 1
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)

        ret = []
        for level in sumAndCount:
            ret.append(sumAndCount[level][0]/sumAndCount[level][1])
        return ret