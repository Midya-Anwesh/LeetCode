class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if (not i) or (not j):
                    ret = max(ret, matrix[i][j])
                else:
                    if matrix[i][j]:
                        matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
                        ret = max(ret, matrix[i][j])
        # print(*matrix, sep = "\n")
        return ret*ret