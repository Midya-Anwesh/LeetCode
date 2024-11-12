class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        # Function to find if a price exists in items if not then it's closest smallest price is returned
        def findAbsoluteOrClosest(items: List[List[int]], price: int) -> int:
            ret = -float('inf')
            st, end = 0, len(items) - 1
            while (st <= end):
                mid = st + (end-st)//2
                if items[mid][0] == price:
                    return items[mid][0]
                elif items[mid][0] > price:
                    end = mid-1
                else:
                    ret = max(ret, items[mid][0])
                    st = mid+1
            return ret

        # Get max bueaty possible for a certain price
        items.sort() # Sorting, to make the next step (normalization) easy
        priceToBeauty = dict()
        for item in items:
            price, beauty = item
            priceToBeauty[price] = max(priceToBeauty.get(price, -float('inf')), beauty)

        # Normalize results, if less price gets more beauty then change the beauty of current price
        prevMaxBeauty = -float('inf')
        for price in priceToBeauty:
            priceToBeauty[price] = max(prevMaxBeauty, priceToBeauty[price])
            prevMaxBeauty = max(prevMaxBeauty, priceToBeauty[price])

        ret = []
        for query in queries:
            # Append maximum beauty possible in current price if not then 0
            ret.append(priceToBeauty.get(findAbsoluteOrClosest(items, query), 0))
        return ret
        