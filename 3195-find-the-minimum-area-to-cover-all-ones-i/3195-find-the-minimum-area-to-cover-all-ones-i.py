class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        Remeber, In this case we can determine the area of the rectangle
        Using two co-ordinates (top left and bottom right)
        suppose we have the co-ordinate as [top, left, bottom, right]
        then the area will be -> (bottom - top + 1) * (right - left + 1)
        """
        top, left, bottom, right = -1, -1, -1, -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    top = min(top, i) if top != -1 else i
                    left = min(left, j) if left != -1 else j

                    bottom = max(bottom, i) if bottom != -1 else i
                    right = max(right, j) if right != -1 else j
        return (bottom - top + 1) * (right - left + 1)