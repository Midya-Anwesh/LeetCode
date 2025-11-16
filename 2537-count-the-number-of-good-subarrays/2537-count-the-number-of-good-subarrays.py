from math import comb
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        goodSubs, win_st, currPairs = 0, 0, 0
        freq = dict()
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            currPairs = currPairs - comb(freq[nums[i]]-1, 2) + comb(freq[nums[i]], 2)
            while currPairs >= k:
                count = freq[nums[win_st]]
                temp = currPairs - comb(count, 2) + comb(count-1, 2)
                if temp >= k:
                    freq[nums[win_st]] -= 1
                    win_st += 1
                    currPairs = temp
                else:
                    break
            if currPairs >= k:
                goodSubs += win_st + 1
        return goodSubs