class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def isSorted(arr):
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    return False
            return True
        
        dels = 0
        curr = ["" for _ in range(len(strs))]
        for j in range(len(strs[0])):
            curr2 = curr[:]
            for i in range(len(strs)):
                curr2[i] += strs[i][j]
            if isSorted(curr2):
                curr = curr2[:]
            else:
                dels += 1
        return dels