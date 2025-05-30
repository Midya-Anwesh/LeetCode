from collections import defaultdict
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # Map to store distance from node1 and node2 to current node
        # i.e: distance[node] = (d1, d2), signifies --> d1 is the distance of node from node1
        #                                               d2 is the distance of node from node2
        distance = defaultdict(lambda:[float('inf'), float('inf')])

        # Function to traverse the graph from a specified node filling distance map accordingly
        def getDistances(source: int, currDis: int) -> None:
            seen = set()
            def dfs(currNode: int, currDis: int) -> None:
                if currNode in seen:
                    return
                seen.add(currNode)
                if source == node1:
                    distance[currNode][0] = min(distance[currNode][0], currDis)
                if source == node2:
                    distance[currNode][1] = min(distance[currNode][1], currDis)
                if edges[currNode] == -1:
                    return
                dfs(edges[currNode], currDis+1)
            dfs(source, 0)
        
        # Fill the distance map from node1 and node2 respectively
        getDistances(node1, 0)
        getDistances(node2, 0)

        # Now check which node is close to both nodes (node1 & node2)
        prevCloseNode, prevCloseDistance = None, float('inf')
        for node in distance:
            if float('inf') in distance[node]:
                continue
            if max(distance[node]) < prevCloseDistance:
                prevCloseNode, prevCloseDistance = node, max(distance[node])
            elif prevCloseDistance == max(distance[node]):
                prevCloseNode = min(prevCloseNode, node)
                
        # Check if it is reachable from node1 and node2 both, if not return -1
        return -1 if prevCloseDistance is float('inf') else prevCloseNode