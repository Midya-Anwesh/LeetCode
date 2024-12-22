from heapq import heapify, heappush, heappop
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        storedQueries, maxIndex, ans = [[] for _ in range(len(heights))], [], [-1]*len(queries)
        heapify(maxIndex)
        """
        storedQueries to store queries according to their right-most index
        maxIndex is heap to process ans of storedQueries
        ans is output vector

        """
        for idx, query in enumerate(queries):
            # If one of them is in tallest building which is situated right of the smaller building
            # Then ans is the index of tallest building
            if heights[max(query)] > heights[min(query)]:
                ans[idx] = max(query)

            # Elif both of them are in the same building from the first
            # Then index of that building is the ans
            elif query[0] == query[1]:
                ans[idx] = query[0]
            
            # Else store the query in storedQueries as a tuple of
            # (height of tallest building as per the query, index of right most building as per the query)
            else:
                storedQueries[max(query)].append( (max(heights[query[0]], heights[query[1]]), idx ) )

        # Traverse heights array for furthur processing
        for idx, height in enumerate(heights):
            # If current height is greater than height in the heap
            # Then it is the ans for that query
            while len(maxIndex) and maxIndex[0][0] < height:
                _, ans_idx = heappop(maxIndex)
                ans[ans_idx] = idx
            # Append queries whose specified right most index is just traversed
            # Also I don't know why we have to do this
            for query in storedQueries[idx]:
                heappush(maxIndex, query)
        
        return ans