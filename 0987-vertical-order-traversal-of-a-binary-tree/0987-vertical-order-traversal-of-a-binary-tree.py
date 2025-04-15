from heapq import heappush, heappop
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        verticalOrder = []
        def traverse(row: int, col: int, root: Optional[TreeNode]) -> None:
            if root is None:
                return
            heappush(verticalOrder, (col, row, root.val))
            traverse(row+1, col-1, root.left)
            traverse(row+1, col+1, root.right)
        traverse(0, 0, root)

        ret, currCol = [], -float('inf')
        while len(verticalOrder):
            col, row, val = heappop(verticalOrder)
            if col != currCol:
                ret.append([val])
                currCol = col
            else:
                ret[-1].append(val)
        return ret