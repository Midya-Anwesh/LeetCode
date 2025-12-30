class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_valid(row: int, col: int) -> bool:
            seen = set()
            s = [0, 0, 0]
            for i in range(row, row + 3):
                s.append(0)
                for j in range(col, col + 3):
                    if not (1 <= grid[i][j] <= 9):
                        return False  # Invalid
                    if grid[i][j] in seen:
                        return False  # Invalid
                    seen.add(grid[i][j])
                    s[-1] += grid[i][j]
                    s[j%3] += grid[i][j]
            i, j = row, col
            s.append(grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2])
            s.append(grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j])
            return len(set(s)) == 1

        magic_grids = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[i]) - 2):
                magic_grids += int(is_valid(i, j))

        return magic_grids
