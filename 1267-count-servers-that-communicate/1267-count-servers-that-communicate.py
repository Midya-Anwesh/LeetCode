class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        seen = [[0]*len(grid[0]) for _ in range(len(grid))]
        connected = 0
        # Check rows first
        for i in range(len(grid)):
            # First two are to point out position of first computer in current row
            # comAll is count of all computer in current row
            # comSeen is count of all computer in current row that are previously seen
            # So, current row will have (comAll-comSeen) new computer connected
            frow, fcol, comAll, comSeen = None, None, 0, 0
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if frow is None and fcol is None:
                        frow, fcol = i, j
                    comAll += 1
                    comSeen += 1 if seen[i][j] else 0
                    seen[i][j] += 1
            
            # IF there is only one computer in the whole row, then we are going to make it unseen
            if comAll == 1:
                seen[frow][fcol] -= 1
            elif comAll > 1:
                connected += comAll - comSeen
        
        # Now do the same for all columns
        for j in range(len(grid[0])):
            frow, fcol, comAll, comSeen = None, None, 0, 0
            for i in range(len(grid)):
                if grid[i][j]:
                    if frow is None and fcol is None:
                        frow, fcol = i, j
                    comAll += 1
                    comSeen += 1 if seen[i][j] else 0
                    seen[i][j] += 1
            if comAll == 1:
                seen[frow][fcol] -= 1
            elif comAll > 1:
                connected += comAll - comSeen
        
        return connected