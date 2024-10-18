class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #fresh orenges will contain position of orenge and time taken to rot, rotten orenges will contain positions only
        fresh_orenges, rottten_orenges, no_of_rotten_orenges, no_of_fresh_orenges = dict(), set(), 0, 0

        # Traverse the matrix and initialize all dict and veriables
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                match(grid[i][j]):
                    case 1:
                        # if orenge is fresh initialize time taken to rot it is inf
                        no_of_fresh_orenges += 1
                        fresh_orenges[(i, j)] = float('inf')
                    case 2:
                        # if orenge is rotten memorize it's position
                        no_of_rotten_orenges += 1
                        rottten_orenges.add((i, j))
        # 
        if no_of_rotten_orenges == 0:
            return -1
        elif no_of_fresh_orenges == 0:
            return 0

        def rot(row: int, col: int, cost: int = 0) -> None:
            nearby = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            for orenge in nearby:
                if orenge in fresh_orenges and fresh_orenges[orenge] > cost+1:
                    fresh_orenges[orenge] = cost+1
                    rot(orenge[0], orenge[1], fresh_orenges[orenge])
        
        for orenge in rottten_orenges:
            rot(orenge[0], orenge[1])
        
        time = 0
        for orenge in fresh_orenges:
            if fresh_orenges[orenge] == float('inf'):
                return -1
            time = max(time, fresh_orenges[orenge])
        return time
        