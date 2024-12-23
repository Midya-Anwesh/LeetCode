from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levelWiseNodes = defaultdict(list)
        def bfs(root: Optional[TreeNode]) -> None:
            nonlocal levelWiseNodes
            deq = deque()
            deq.append((root, 0))
            while len(deq):
                node, level = deq.popleft()
                levelWiseNodes[level].append(node.val)
                if node.left is not None:
                    deq.append((node.left, level+1))
                if node.right is not None:
                    deq.append((node.right, level+1))
        bfs(root)

        ret = 0
        def minSwaps(arr1: List[int], arr2: List[int]) -> int:
            swaps = 0
            elements = {arr1[i]:i for i in range(len(arr1))}
            for i in range(len(arr2)):
                if arr1[i] != arr2[i]:
                    idx = elements[arr2[i]]
                    arr1[i], arr1[idx] = arr1[idx], arr1[i]
                    elements[arr1[i]], elements[arr1[idx]] = i, idx
                    swaps += 1
            return swaps

        for level in levelWiseNodes:
            ret += minSwaps(levelWiseNodes[level], sorted(levelWiseNodes[level]))
        return ret