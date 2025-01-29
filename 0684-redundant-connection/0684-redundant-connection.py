class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0]*1001
        parent = list(range(1001))

        def union(source: int, destination: int) -> None:
            if rank[source] == rank[destination]:
                sourceUparent = findUparent(source)
                destinationUparent = findUparent(destination)
                source = sourceUparent
                destination = destinationUparent

            if rank[source] < rank[destination]:
                parent[source] = destination
            
            else:
                parent[destination] = source
        
        def findUparent(vertex: int) -> int:
            if parent[vertex] == vertex:
                return vertex
            parent[vertex] = findUparent(parent[vertex])
            return parent[vertex]
        
        ret = None
        for source, destination in edges:
            if findUparent(source) == findUparent(destination):
                ret = [source, destination]
            union(source, destination)
        
        return ret