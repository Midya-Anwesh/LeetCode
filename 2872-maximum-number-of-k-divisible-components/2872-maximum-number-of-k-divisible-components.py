from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        connections = defaultdict(list)
        start = 0
        for edge in edges:
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])
        seen = set()
        ret = 0
        def dfs(vertex: int) -> int:
            nonlocal ret
            seen.add(vertex)
            sumVal = values[vertex]
            for node in connections[vertex]:
                if node in seen:
                    continue
                sumVal += dfs(node)
            if not sumVal%k:
                ret += 1
                return 0
            return sumVal
        dfs(0)

        return ret