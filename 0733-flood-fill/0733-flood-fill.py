ADJ = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(row: int, col: int, srcCol: int, dstCol: int) -> None:
            image[row][col] = dstCol
            for dx, dy in ADJ:
                nr, nc = row+dx, col+dy
                if nr < 0 or nr >= len(image) or nc < 0 or nc >= len(image[0]) or image[nr][nc] != srcCol:
                    continue
                dfs(nr, nc, srcCol, dstCol)
        if image[sr][sc] != color:
            dfs(sr, sc, image[sr][sc], color)
        return image