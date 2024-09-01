# runtime = 484.0ms
# memory usage = 29.8MB

class Solution:

    def maxOperations(self, nums: list[int], k: int) -> int:

        ret,d = 0,dict()

        for num in nums:

            d[num]=d.get(num,0)+1

        for num in d:

            while d[num] and d.get(k-num,0):

                if num == k-num and d[num] < 2:

                    break

                ret += 1

                d[num] -= 1

                d[k-num] -= 1

        return ret

        