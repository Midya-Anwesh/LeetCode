from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorToNums = defaultdict(set)
        colorOfNum = dict()

        ans = []
        for x, y in queries:
            # If ball x is previously colored
            if x in colorOfNum:
                # Remove ball x from set of balls having color of colorOfNum[x]
                colorToNums[colorOfNum[x]].discard(x)
                # If it was the last ball of the color then remove the color
                if not len(colorToNums[colorOfNum[x]]):
                    colorToNums.pop(colorOfNum[x])
            # Re-paint ball x with color y
            colorOfNum[x] = y
            # Add ball x to the set of balls having color y
            colorToNums[y].add(x)
            
            # Length of colorToNums will answer distinct colors left after each query
            ans.append(len(colorToNums))
        
        return ans