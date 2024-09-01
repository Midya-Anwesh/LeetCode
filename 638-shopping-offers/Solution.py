# runtime = 77.0ms
# memory usage = 16.6MB

from math import inf

class Solution:
    def valid(self, need, curr):
        return all(curr[i] <= need[i] for i in range(len(need)))

    def remaining(self, need, curr):
        return [need[i]-curr[i] for i in range(len(need))]

    def mul(self, need, curr):
        ret = 0
        for i in range(len(curr)):
            ret += need[i]*curr[i]
        return ret

    def check(self, price, special, need, cost = inf):
        curr, f, key = inf, True, tuple(need)
        if key in self.memo:
            return self.memo[key]
        for info in special:
            if self.valid(need, info):
                f = False
                curr = info[-1]
                curr += self.check(price, special, self.remaining(need, info))
                cost = min(cost, curr)
        self.memo[key] = self.mul(need, price) if f else min(cost, self.mul(need, price))
        return self.memo[key]

    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        self.memo = dict()
        return self.check(price, special, needs)