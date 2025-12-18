class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prefix = [0]
        for price, s in zip(prices, strategy):
            prefix.append(prefix[-1] + price * s)

        win_st, win_sum, win_end = 0, 0, k
        for i in range(k//2, k):
            win_sum += prices[i]

        maxProfit = max(prefix[-1], prefix[-1] - (prefix[k] - prefix[win_st]) + win_sum)

        while win_end < len(strategy):
            win_sum -= prices[win_st+(k//2)]
            win_st += 1
            win_sum += prices[win_end]
            win_end += 1
            maxProfit = max(maxProfit, prefix[-1] - (prefix[win_end] - prefix[win_st]) + win_sum )
        
        return maxProfit
