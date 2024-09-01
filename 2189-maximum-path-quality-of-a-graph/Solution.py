# runtime = 1222.0ms
# memory usage = 17.7MB

from collections import defaultdict

class Solution:

    

    def dfs(self, t, curr = 0,vis=[]):

        vis.append(curr)

        if vis[-1] == 0:

            self.ret = max(self.ret, sum(self.values[i] for i in set(vis)))

        

        for edge in self.edges[curr]:

            if edge[-1] <= t:

                vertex = edge[1-edge.index(curr)]

                self.dfs(t-edge[-1], vertex, vis)

                vis.pop(-1)

    

    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:

        self.edges = defaultdict(lambda:[])

        self.ret = -float('inf')

        self.values = values

        for edge in edges:

            self.edges[edge[0]].append(edge)

            self.edges[edge[1]].append(edge)

        self.dfs(maxTime)

        return self.ret

        