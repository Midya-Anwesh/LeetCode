from collections import defaultdict
from heapq import heappush, heappop
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # shopHeap maps movie to heap of stores which offer the movie
        # each element in that heap is (price, shopId)
        self.shopHeap = defaultdict(list)

        # shopsInHeap keeps record of which shops are servicing a specific movie
        # If maps a movie to a set of shop ids which services that movie
        self.shopsInHeap = defaultdict(set)

        # priceOfMovie keeps record of how much a movie cost at a specified shop
        # (movie, shopId) -> price
        self.priceOfMovie = dict()

        # copiesInShop maps (shopId, movie) -> no of copies available
        self.copiesInShop = defaultdict(int)

        # cheapRents will keep track of rents on the besis of prices
        self.cheapRents = []

        # Rentals will keep track of currently rented movies
        # All enteries will be like (shopId, movie)
        self.rentals = set()

        # Now fill the structures with incoming entries
        for shopId, movie, price in entries:
            heappush(self.shopHeap[movie], (price, shopId))
            self.shopsInHeap[movie].add(shopId)
            self.priceOfMovie[(movie, shopId)] = price
            self.copiesInShop[(shopId, movie)] = 1

    def search(self, movie: int) -> List[int]:
        ret = [] # return vector
        temp = [] # Temp heap to recover the original later
        # For search we will pop elements from shopHeap
        while len(self.shopHeap[movie]) and (len(ret) < 5):
            price, shopId = heappop(self.shopHeap[movie])
            # If copies of that movie is available only then add that shop to ret
            # And only then push the entry to temp heap
            # Otherwise remove the shop from heap
            copiesAvailable = self.copiesInShop[(shopId, movie)]
            if copiesAvailable >= 1:
                ret.append(shopId)
                heappush(temp, (price, shopId))
            else:
                self.shopsInHeap[movie].remove(shopId)
        # Recover the original heap
        while len(temp):
            heappush(self.shopHeap[movie], heappop(temp))
        # Return the vector
        return ret
        

    def rent(self, shopId: int, movie: int) -> None:
        # Firstly check if copies are availabl or not
        copiesAvailable = self.copiesInShop[(shopId, movie)]
        if copiesAvailable >= 1:
            # Get the cost of the movie at the shop
            price = self.priceOfMovie[(movie, shopId)]
            # Add the movie to cheapRentals and maintain the size, if it's not in there previously
            if (shopId, movie) not in self.rentals:
                heappush(self.cheapRents, ((price, shopId, movie)))
                # Record it as rented
                self.rentals.add((shopId, movie))
            # Reduce number of copies
            self.copiesInShop[(shopId, movie)] -= 1

    def drop(self, shopId: int, movie: int) -> None:
        # Drop entry from rentals
        self.rentals.remove((shopId, movie))
        # Firstly get what the movie costs in that shop
        price = self.priceOfMovie[(movie, shopId)]
        # Increase no of copies available for the movie in that shop
        self.copiesInShop[(shopId, movie)] += 1
        # If, previously the shop was not in the heap of that movie then add it now
        if shopId not in self.shopsInHeap[movie]:
            self.shopsInHeap[movie].add(shopId)
            heappush(self.shopHeap[movie], (price, shopId))

    def report(self) -> List[List[int]]:
        # Return vector
        ret = []
        # temp to recover rentals later
        temp = []
        # Now traverse the rentals heap
        while len(self.cheapRents) and (len(ret) < 5):
            price, shopId, movie = heappop(self.cheapRents)
            # If the movie is rented only then add it
            if ((shopId, movie) in self.rentals) and ((shopId, movie) not in ret):
                ret.append((shopId, movie))
                temp.append((price, shopId, movie))
        # Recover rentals
        while len(temp):
            heappush(self.cheapRents, temp.pop())
        # Return the ans vector
        return ret


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()