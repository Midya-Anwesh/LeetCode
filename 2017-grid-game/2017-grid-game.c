# pragma GCC optimize("O2")

long long gridGame(int** grid, int gridSize, int* gridColSize) {
    // Build prefix sum for both rows 0 and 1
    long long *pSum0 = (long long*)calloc(sizeof(long long), (*gridColSize)+1), *pSum1 = (long long*)calloc(sizeof(long long), (*gridColSize)+1);

    // Fill prefix sum arrays
    for(int i = 1; i <= *gridColSize; i++){
        pSum0[i] = pSum0[i-1]+grid[0][i-1];
        pSum1[i] = pSum1[i-1]+grid[1][i-1];
    }

    // Return variable
    long long ans = LLONG_MAX;

    for (int i = 0; i < (*gridColSize); i++){
        /* Consider if robot 1 goes to next row from current row at index i
           What will the max that robot 2 will be able to collect
        */

        // Calculate what is left in row0
        long long row0left = pSum0[(*gridColSize)] - pSum0[i] - grid[0][i];
        // Calculate what is left in row1
        long long row1left = pSum1[i];
        
        // As robots can only go right ans down, so robot2 will be able to collect max of those two
        // We will take the minimum of every possibility
        ans = (ans > ((row0left > row1left) ? row0left:row1left)) ? ((row0left > row1left) ? row0left:row1left):ans;

    }
    // Return max points collected by robot2
    return ans;
}