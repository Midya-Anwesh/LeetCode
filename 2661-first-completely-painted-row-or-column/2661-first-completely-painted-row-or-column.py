class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Hash map which maps element to its row and col, dict[ele] = (row, col)
        rowCol = {mat[i][j]:(i, j) for i in range(len(mat)) for j in range(len(mat[0]))}

        # Creat a row and col array to see how much filled a row and col is
        row = [0] * len(mat)
        col = [0] * len(mat[0])

        # Return variable
        ret = float('inf')

        # Traverse the elements of arr
        for i, num in enumerate(arr):

            # Get the row and col position of the element and fill them
            r, c = rowCol[num]
            row[r] += 1
            col[c] += 1

            # If current row is filled, then choose minimum between ret and row
            if row[r] == len(mat[0]):
                ret = min(ret, i)
            
            # If current col is filled, then choose minimum between ret and col
            if col[c] == len(mat):
                ret = min(ret, i)

            # If any row and col is filled no need to check more
            if ret < float('inf'):
                break
        
        return ret