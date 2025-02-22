# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        level = [0]
        nodeVal = []
        index = 0
        num = ""
        while traversal[index].isdigit():
            num += traversal[index]
            index += 1
        nodeVal.append(int(num))

        while index < len(traversal):
            if traversal[index] == "-":
                currLevel = 0
                while index < len(traversal) and traversal[index] == "-":
                    currLevel += 1
                    index += 1
                level.append(currLevel)
            
            else:
                num = ""
                while index < len(traversal) and traversal[index].isdigit():
                    num += traversal[index]
                    index += 1
                nodeVal.append(int(num))
        
        top = 1
        root = TreeNode(nodeVal[0])
        addedAll = False

        def addNode(root: Optional[TreeNode], currLevel: int) -> None:
            nonlocal top, addedAll
            if (top >= len(level)):
                addedAll = True
                return

            if (level[top] == currLevel+1):
                root.left = TreeNode(nodeVal[top])
                top += 1
                addNode(root.left, currLevel+1)
                if addedAll:
                    return

            elif (level[top] < currLevel+1):
                return
            
            if (level[top] == currLevel+1):
                root.right = TreeNode(nodeVal[top])
                top += 1
                addNode(root.right, currLevel+1)
        addNode(root, 0)
        
        return root