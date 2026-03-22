class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        flags = [True, True, True, True] # [0, 90, 180, 270]
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    flags[0] = False
                if mat[j][n-i-1] != target[i][j]:
                    flags[1] = False
                if mat[n-i-1][n-j-1] != target[i][j]:
                    flags[2] = False
                if mat[n-j-1][i] != target[i][j]:
                    flags[3] = False
        return any(flags)