class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = sorted(arr)
        res = 1

        def partition(index: int, curr: List[List[int]]) -> None:
            nonlocal res
            if index == len(arr):
                temp = []
                for part in curr:
                    temp += [*part]
                if temp == ans:
                    res = max(res, len(curr))
                return

            for i in range(index, len(arr)):
                curr.append(sorted(arr[index:i+1]))
                partition(i+1, curr)
                curr.pop()
        
        partition(0, [])
        return res