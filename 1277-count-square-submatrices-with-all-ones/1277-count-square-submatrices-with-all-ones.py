class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ret = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (not i) or (not j):
                    ret += matrix[i][j]
                else:
                    if matrix[i][j]:
                        matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
                        ret += matrix[i][j]
        
        return ret