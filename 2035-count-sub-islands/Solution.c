// runtime = 298.0ms
// memory usage = 33.6MB

void visiteIsland(int i, int j, int **grid1, int **grid2, int row, int col, int *is_sub){
    
    *is_sub = (*is_sub)*grid1[i][j];
    grid2[i][j] = 0;
    
    if (i > 0 && grid2[i-1][j]){
        visiteIsland(i-1, j, grid1, grid2, row, col, is_sub);
    }
    
    if (i < row-1 && grid2[i+1][j]){
        visiteIsland(i+1, j, grid1, grid2, row, col, is_sub);
    }
    
    if (j > 0 && grid2[i][j-1]){
        visiteIsland(i, j-1, grid1, grid2, row, col, is_sub);
    }
    
    if (j < col-1 && grid2[i][j+1]){
        visiteIsland(i, j+1, grid1, grid2, row, col, is_sub);
    }
}

int countSubIslands(int** grid1, int grid1Size, int* grid1ColSize, int** grid2, int grid2Size, int* grid2ColSize) {
    int subIslands = 0;
    for (int i = 0; i < grid2Size; i++){
        for (int j = 0; j < *grid2ColSize; j++){
            if (!grid2[i][j]){
                continue;
            }
            int is_sub = grid1[i][j];
            
            visiteIsland(i, j, grid1, grid2, grid2Size, *grid2ColSize, &is_sub);
            
            subIslands += is_sub;
        }
    }
    return subIslands;
}