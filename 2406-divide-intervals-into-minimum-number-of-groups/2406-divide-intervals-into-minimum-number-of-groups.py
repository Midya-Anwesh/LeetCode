class TreeNode:
    def __init__(self, interval: List[List[int]]) -> None:
        self.interval = interval
        self.left = None
        self.right = None
    def overlap(self, interval: List[List[int]]) -> bool:
        return (self.interval[0] <= interval[0] <= self.interval[1]) or \
        (self.interval[0] <= interval[1] <= self.interval[1])

class Solution:
    def addInterval(self, root: TreeNode, interval: List[List[int]]) -> int:
        while (root.overlap(interval)):
            if interval[0] <= root.interval[0]:
                if root.left is None:
                    root.left = TreeNode(interval)
                    return 1
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = TreeNode(interval)
                    return 1
                else:
                    root = root.right
        root.interval = interval
        return 0

    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        ans, root = 1, TreeNode(intervals[0])
        for i in range(1, len(intervals)):
            ans += self.addInterval(root, intervals[i])
        return ans