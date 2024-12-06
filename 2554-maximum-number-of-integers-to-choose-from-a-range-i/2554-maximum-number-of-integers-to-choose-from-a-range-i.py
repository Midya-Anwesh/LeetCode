class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ret, s = 0, 0
        for num in range(1, n+1):
            if num in banned:
                continue
            elif (s:=s+num) <= maxSum:
                ret += 1
            else:
                break
        return ret