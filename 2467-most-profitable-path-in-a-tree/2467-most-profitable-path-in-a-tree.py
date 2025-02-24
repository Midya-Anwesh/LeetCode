from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjNodes = defaultdict(set)
        for u, v in edges:
            adjNodes[u].add(v)
            adjNodes[v].add(u)
        
        amount = {i:[amount[i], float('inf')] for i in range(len(amount))}
        reachedRoot = False
        seen = set()
        def moveBob(currNode: int, time: int) -> None:
            seen.add(currNode)
            amount[currNode][1] = time # Bob is at node 'currNode' at time 'time'
            for node in adjNodes[currNode]:
                if not (node in seen):
                    moveBob(node, time+1)
                    if 0 in seen: # If we can go to root following current path then return
                        return
                    amount[node][1] = float('inf') # Else set the time-stamp of the recently traverces node to inf and try other adj nodes
        moveBob(bob, 0)

        seen = set()
        def getMostProfit(currNode: int, time: int) -> int:
            seen.add(currNode)
            curr = None
            if time < amount[currNode][1]: # If Alice gets to currNode before Bob
                curr = amount[currNode][0]
            elif time > amount[currNode][1]: # If Bob gets to currNode before Alice
                curr = 0
            else: # If Both gets to currNode at the same time
                curr = amount[currNode][0] // 2
            
            if currNode and len(adjNodes[currNode]) == 1:
                return curr
            
            nextMax = -float('inf')
            for node in adjNodes[currNode]:
                if not (node in seen):
                    nextMax = max(nextMax, getMostProfit(node, time+1))
                    seen.discard(node)
            return curr + (nextMax if nextMax > -float('inf') else 0)
            
        return getMostProfit(0, 0)