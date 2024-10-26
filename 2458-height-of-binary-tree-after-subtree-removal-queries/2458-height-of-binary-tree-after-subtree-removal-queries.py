# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        from heapq import heapify, heappush, heappop

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        level_wise_heap, get_level = dict(), dict()
        def dfs(root : Optional[TreeNode], level: int) -> int:
            if root is None:
                return 0
            get_level[root.val] = level
            left_height = dfs(root.left, level+1)
            right_height = dfs(root.right, level+1)
            if not level in level_wise_heap:
                level_wise_heap[level] = []
                heapify(level_wise_heap[level])
            heappush(level_wise_heap[level], [-1*max(left_height, right_height), root.val])
            return max(left_height+1, right_height+1)
        dfs(root, 0)
        
        ret, root_height = [], heappop(level_wise_heap[0])[0]*-1
        for query in queries:
            height, node = heappop(level_wise_heap[get_level[query]])
            if node == query:
                if not len(level_wise_heap[get_level[query]]):
                    ret.append(get_level[query])
                next_max_height, next_effective_node = heappop(level_wise_heap[get_level[query]])
                ret.append(get_level[query]+(next_max_height*-1))
                heappush(level_wise_heap[get_level[query]], [next_max_height, next_effective_node])
            else:
                ret.append(root_height)
            heappush(level_wise_heap[get_level[query]], [height, node])
        return ret