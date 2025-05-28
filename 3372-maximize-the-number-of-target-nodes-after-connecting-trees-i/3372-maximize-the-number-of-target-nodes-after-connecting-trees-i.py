class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """
        As per the question,
        A node can target another node which is at most k edges away

        So, for each node in tree1, 
            We need to find number of nodes which are at most k edges away

        We can also join a node from tree1 to tree2,
            By doing this we will be adding 1 additional edge to go to tree2
            Suppose we join node1 of tree1 with node2 of tree2,
                Now, all the nodes which are at most k-1 edges away from node2 will be a target
                We, don't need to search in tree1 from node2 as node1 has larger range in tree1
                (node1 will target more nodes in tree1 including which can be targeted by node2)
            Thus, if we find a node in tree2 which can target maximum nodes in tree2, we will always connect to that node from tree1
            As, no other node in tree2 will increase the number of targets
        
        Hence, we can comclude that
        For tree1:
            Find maximum number of nodes that can be targeted from each node
        For tree2:
            Find a node which can target maximum node in tree2 (maxNode)
        
        Now, for each node in tree1 do
        sum(Number of nodes targetted in tree1 from current node, number of nodes targetted in tree2 by maxNode)
        """
        # Build the graph1/tree1
        tree1 = defaultdict(list)
        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        # Build the graph2/tree2
        tree2 = defaultdict(list)
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)

        # Function to find number of target node from a specified node, which are at most specified edges away
        def findNoOfTargets(tree: Dict[int, List[int]], curr: int, k: int) -> int:
            if k < 0:
                return 0
            elif not k:
                return 1
            targetNodes = set()
            def dfs(curr: int, k: int) -> None:
                targetNodes.add(curr)
                if not k:
                    return
                for adjNode in tree[curr]:
                    if adjNode not in targetNodes:
                        dfs(adjNode, k-1)
                return
            dfs(curr, k)
            return len(targetNodes)

        # Map to store number of nodes that can be targetted in tree1 from each node in tree1
        targetT1 = dict()
        for node in range(len(edges1)+1):
            targetT1[node] = findNoOfTargets(tree1, node, k)
        # Find maxNode in tree2
        maxNode, targetCount = 0, findNoOfTargets(tree2, 0, k-1)
        for node in range(1, len(edges2)+1):
            if (count := findNoOfTargets(tree2, node, k-1)) > targetCount:
                maxNode, targetCount = node, count
        # Result vector ret
        ret = []
        # For each node in tree1 find number of targets
        for node in range(len(edges1)+1):
            ret.append(targetT1[node]+targetCount)
        return ret