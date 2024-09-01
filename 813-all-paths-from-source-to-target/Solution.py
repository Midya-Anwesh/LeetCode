# runtime = 71.0ms
# memory usage = 17.0MB

class Solution:
    def get_all_path(self, graph: list[list[int]], n: int, path: list[int], s: int = 0):
        path.append(s)
        if s == n-1:
            yield path
            return
        
        for vertex in graph[s]:
            yield from self.get_all_path(graph, n, path, vertex)
            path.pop(-1)
            
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        yield from self.get_all_path(graph, len(graph), [])
        