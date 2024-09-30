from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def is_safe(self, curr: int):
        if not len(self.graph[curr]):
            return True
        if curr in self.seen:
            return False
        self.seen.update({curr:"seen"})
        for node in self.graph[curr]:
            if node == curr or (not (self.is_safe(node))):
                return False
        return True
            
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.graph, self.seen = graph, dict()
        for i in range(len(graph)):
            if (self.is_safe(i)):
                yield i
            self.seen.clear()