class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = {num:0 for num in arr}
        ret = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                length = 2
                fnm1, fnm2 = arr[j], arr[i]
                while (fn := fnm1 + fnm2) in nums:
                    length += 1
                    fnm1, fnm2 = fn, fnm1
                ret = max(ret, length)
        return ret if ret > 2 else 0