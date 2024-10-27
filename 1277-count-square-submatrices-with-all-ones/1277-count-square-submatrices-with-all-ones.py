class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(300)] for _ in range(300)]
        ret = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]:
                    matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret += matrix[i][j]
        
        return ret