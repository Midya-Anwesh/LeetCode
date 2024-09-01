# runtime = 54.0ms
# memory usage = 16.7MB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, comb, tot):
            if tot == target:
                ans.append(comb[:])
                return
            if i >= len(candidates) or tot > target:
                return
            comb.append(candidates[i])
            backtrack(i, comb, tot + candidates[i])
            comb.pop()
            backtrack(i + 1, comb, tot)
        backtrack(0, [], 0)
        return ans