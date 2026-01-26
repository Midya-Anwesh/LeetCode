class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ret, minDiff = [], float('inf')
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < minDiff:
                ret = [[arr[i], arr[i+1]]]
                minDiff = arr[i+1]-arr[i]
            elif arr[i+1]-arr[i] == minDiff:
                ret.append( [arr[i], arr[i+1]] )
        return ret