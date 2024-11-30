class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # in_out_count to count number of ingoing and outgoing edges
        # vertex: [ingoing count, outgoing count]

        # connected_edges to track which edges are connected to which node
        # vertex: [ [vertex, destination] ]
        m = max(pairs, key=lambda edge:max(edge))
        in_out_count, connected_edges = defaultdict(lambda:[0,0]), defaultdict(lambda:deque([]))

        for edge in pairs:
            connected_edges[edge[0]].append(edge)
            in_out_count[edge[0]][1] += 1
            in_out_count[edge[1]][0] += 1
        
        # As we are told testcases are designed such that they have euler path
        start = pairs[0][0] # We consider first node as start point

        for vertex in in_out_count:
            # If any node has one more outgoing edge than incoming then that will be start node
            if in_out_count[vertex][1] - in_out_count[vertex][0] == 1:
                start = vertex

        ret = []
        def hierholzer(vertex: int, prev: None|int) -> None:
            while len(connected_edges[vertex]):
                edge = connected_edges[vertex].popleft()
                hierholzer(edge[1], vertex)
            if prev is not None:
                ret.append([prev, vertex])
        hierholzer(start, None)
        
        for i in range(len(ret)//2):
            ret[i], ret[-(i+1)] = ret[-(i+1)], ret[i]
        
        return ret