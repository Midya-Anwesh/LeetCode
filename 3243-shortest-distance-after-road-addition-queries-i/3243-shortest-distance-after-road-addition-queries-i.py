class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        def dijkstra(vertex: int) -> None:
            for adj_vertex in connections[vertex]:
                if distances[adj_vertex] > distances[vertex]+1:
                    distances[adj_vertex] = distances[vertex]+1
                    dijkstra(adj_vertex)

        connections = dict()
        for i in range(n):
            if i < n-1:
                connections[i] = [i+1]
            else:
                connections[i] = []

        distances = {i:i for i in range(n)}
        distances[0], ret = 0, []
        for source, destination in queries:
            connections[source].append(destination)
            distances[destination] = min(distances[destination], distances[source]+1)
            dijkstra(destination)
            ret.append(distances[n-1])
        return ret